import os
import sys
import json
import requests
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv
import ast

# Set up system path for package imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

# Importing necessary modules from the image_to_text package
from prompt.prompt import Prompts
# Importing and setting up the generative AI model
import google.generativeai as gai

load_dotenv()
api_key = os.getenv("API_KEY")
gai.configure(api_key=api_key)
model = gai.GenerativeModel('gemini-1.5-flash')

def download_image(image_url:str) -> Image.Image:
    """Download image from URL and return PIL Image."""
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        return img
    except Exception as e:
        print(f"Error downloading image: {e}")
        raise e

def generate_content(image:Image, prompt_type:str):
   
    prompt = getattr(Prompts(), prompt_type)
    generated_content = model.generate_content([prompt, image])
   
    return generated_content.text

def process_image(image_url:str , prompt_type:str):
    
    """Main function to process the image and print the results."""
    img:Image = download_image(image_url)

    if prompt_type == "initial_data_text":
        initial_data_text = generate_content(img, 'initialJSONdataFramePrompt')
        initial_data_text = initial_data_text.strip()  # Remove leading/trailing whitespace
        print(initial_data_text)
        initial_data_text = json.loads(initial_data_text)
        return {
        'initialData': initial_data_text
        }
    elif prompt_type == "ratio_specified_text":
          
       ratio_specified_text =  generate_content(img, 'ratioSpecifiedPrompt')
       print(ratio_specified_text)
       ratio_specified_text = json.loads(ratio_specified_text)
        
       return {
                'ratioSpecified': ratio_specified_text
            }
        
    elif prompt_type == "health_consideration_text":
        healthConsideration_text =  generate_content(img, 'healthPrompt')
        
        healthConsideration_text = json.loads(healthConsideration_text)
        return {
             'healthConsideration': healthConsideration_text
        }
    elif prompt_type == "conclusion_text":
        conclusion_text =  generate_content(img, 'otherPrompt')
        conclusion_text = json.loads(conclusion_text)
        return {
               'conclusionData': conclusion_text
        }



# Example usage

# print(process_image('https://imagehub-n7dz.onrender.com/IMG-20240617-WA0013-1719234482446.jpg', 'initial_data_text'))    

# print(process_image('https://imagehub-n7dz.onrender.com/IMG-20240617-WA0013-1719234482446.jpg', 'ratio_specified_text'))    

# print(process_image('https://imagehub-n7dz.onrender.com/IMG-20240617-WA0013-1719234482446.jpg', 'health_consideration_text'))    

# print(process_image('https://imagehub-n7dz.onrender.com/IMG-20240617-WA0013-1719234482446.jpg', 'conclusion_text'))    
# asyncio.run(process_image('https://m.media-amazon.com/images/I/81iTeA3lETL._AC_UF1000,1000_QL80_.jpg'))

