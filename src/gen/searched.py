import ast
import os
import google.generativeai as gai
import asyncio
import ast

from src.gen.google_search import googleSearchImage
api_key = os.getenv("GOOGLE_API_KEY")

gai.configure(api_key=api_key)
model = gai.GenerativeModel('gemini-1.5-flash')




async def categoriedCall(filterData: list, nutrient: str):
    prompt = PromptManager(filterData, nutrient).get_prompt()  # Get the actual prompt text

    response = model.generate_content(
        prompt,
        generation_config={"temperature": 0.0}
    )

    model_suggestion = ast.literal_eval(response.text)

    listOfNames = [item['name'] for item in model_suggestion if 'name' in item]


    responsedata = await googleSearchImage(listOfNames[0])  # Await the coroutine properly

    listOfImages = await fetch_images_async(listOfNames)
    for item, image_url in zip(model_suggestion, listOfImages):
        item['imageUrl'] = image_url
    
    print(listOfImages)
    return model_suggestion



async def fetch_images_async(names):
    tasks = [googleSearchImage(name) for name in names]  # Directly await async function
    return await asyncio.gather(*tasks)


class PromptManager():

    def __init__(self, filterData:list, nutrients):
        self._prompt = f"""Generate 10 product data available in the Indian market which are similar or have the same properties as {filterData} and {nutrients}. The schema of the data will be like:
            dont add any tag like "```json " in data not even "```" in data
         [
            
         {{
         
             "name": "//name",
            "description": "//description",
            "health_benefits": [
                "//e.g",
                "Rich in protein",
                "//more"
            ],
            "common_uses": [
                "//e.g",
                "Rich in protein",
                "//more"
            ],
            
            "company_name": "company name",
            "price": "//price",
            "qty": "quantity",
            "category": "product category",
            "rating": "product rating",
            "availability": "in stock or out of stock",
           
        }}],
     Note::  no notes and comments are needed and do not provide ```JSON things in all response just provide json to convert that easily
        """
    def get_prompt(self):
        return self._prompt 




