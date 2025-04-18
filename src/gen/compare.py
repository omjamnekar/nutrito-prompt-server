import json
from flask import Flask, request, jsonify
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from prompts.nutrilization_Prompt import Prompts
from prompts.compare import ComparisionPrompts
import google.generativeai as gai

load_dotenv()

# Configure Generative AI model
api_key = os.getenv("GOOGLE_API_KEY")
gai.configure(api_key=api_key)
model = gai.GenerativeModel('gemini-1.5-flash')

def compare_generate_content(image1: Image ,image2:Image):
    prompt = getattr(ComparisionPrompts(), "compareProductsPrompt")
    generated_content = model.generate_content([prompt, image1 ,image2])
    
    # Default for missing data
    if not generated_content.text:
        return {'error': 'Generated content is empty or incomplete'}

    return generated_content.text


def clean_json_input(raw_data):
    """Clean JSON string from unwanted formatting."""
    if raw_data.startswith("```json"):
        raw_data = raw_data.replace("```json", "", 1).strip()
    if raw_data.startswith("```"):
        raw_data = raw_data.replace("```", "", 1).strip()
    if raw_data.endswith("```"):
        raw_data = raw_data[:raw_data.rfind("```")].strip()
    return raw_data

def     comapare_process_image(image1: Image,image2:Image):
    """Process the image based on the prompt type and return JSON."""
    try:

        generated_text = compare_generate_content(image1,image2)
      
        cleaned_text = clean_json_input(generated_text)
        print(cleaned_text)
        return {"compareProducts": json.loads(cleaned_text.strip())}

    except json.JSONDecodeError as e:
        raise ValueError(f"JSON decoding failed for prompt type prompt_type. Error: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error processing image for prompt type prompt_type: {str(e)}")