import ast
import os
import google.generativeai as gai
api_key = os.getenv("GOOGLE_API_KEY")

gai.configure(api_key=api_key)
model = gai.GenerativeModel('gemini-1.5-flash')



def genCall(requestData):
    prompt = PromptManager(requestData).get_prompt()  # Get the actual prompt text

    response = model.generate_content(
        prompt,  # Pass the string, not an object
        generation_config={"temperature": 0.0}
    )
 
    model_suggestion= ast.literal_eval(response.text) 
    return model_suggestion



class PromptManager():

    def __init__(self, product_property):
        self._prompt = f"""Generate 10 product data available in the Indian market which are similar or have the same properties as {product_property}. The schema of the data will be like:
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
            "availability": "in stock or out of stock"
        }}],
     Note::  no notes and comments are needed and do not provide ```JSON things in all response just provide json to convert that easily
        """
    def get_prompt(self):
        return self._prompt 


