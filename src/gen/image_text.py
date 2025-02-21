import os
import sys
import json
from flask import Flask, request,jsonify
# import requests
from PIL import Image
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from prompts.nutrilization_Prompt import Prompts
import google.generativeai as gai
load_dotenv()



api_key = os.getenv("GOOGLE_API_KEY")

gai.configure(api_key=api_key)
model = gai.GenerativeModel('gemini-1.5-flash')

# def download_image(image_url:str) -> Image.Image:
#     """Download image from URL and return PIL Image."""
#     try:
#         response = requests.get(image_url)
#         img = Image.open(BytesIO(response.content))
#         return img
#     except Exception as e:
#         print(f"Error downloading image: {e}")
#         raise e

def generate_content(image:Image, prompt_type:str):
   
    prompt = getattr(Prompts(), prompt_type)
    generated_content = model.generate_content([prompt, image])
   
    return generated_content.text





def process_image(image: Image, prompt_type: str):
   
    try:
        if prompt_type == "initial_data_text":
            initial_data_text = generate_content(image, 'initialJSONdataFramePrompt')
            
            print(f"Initial Data Text: {clean_json_input(initial_data_text)}")
            return {'initialData': json.loads(clean_json_input(initial_data_text).strip())}

        elif prompt_type == "ratio_specified_text":
            ratio_specified_text = generate_content(image, 'ratioSpecifiedPrompt')
            print(f"Ratio-Specified Text: {clean_json_input(ratio_specified_text)}")
            return {'ratioSpecified': json.loads(clean_json_input(ratio_specified_text).strip())}

        elif prompt_type == "health_consideration_text":
            healthConsideration_text = generate_content(image, 'healthPrompt')
            print(f"Health Consideration Text: {healthConsideration_text}")
            return {'healthConsideration': json.loads(clean_json_input(healthConsideration_text).strip())}

        elif prompt_type == "conclusion_text":
            conclusion_text = generate_content(image, 'otherPrompt')
            # print(f"Conclusion Text: {conclusion_text}")
            conclusion_text = conclusion_text.strip()
            if not conclusion_text:
                raise ValueError("Generated content is empty.")
            return {'conclusionData': json.loads(clean_json_input(conclusion_text))}

        else:
            raise ValueError(f"Unknown prompt type: {prompt_type}")

    except json.JSONDecodeError as e:
        raise ValueError(f"JSON decoding failed for prompt type {prompt_type}. Error: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error processing image for prompt type {prompt_type}: {str(e)}")


def clean_json_input(raw_data):
    # Check and remove starting ```json
    if raw_data.startswith("```json"):
        raw_data = raw_data.replace("```json", "", 1).strip()
# Check and remove starting ``` if present
    if raw_data.startswith("```"):
        raw_data = raw_data.replace("```", "", 1).strip()
    # Check and remove trailing ```
    if raw_data.endswith("```"):
        raw_data = raw_data[:raw_data.rfind("```")].strip()
    
    return raw_data