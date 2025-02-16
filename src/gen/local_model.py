import os
import json
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import ast
from src.database.load_Data import loadData
import google.generativeai as gai


api_key = os.getenv("GOOGLE_API_KEY")
gai.configure(api_key=api_key)
client = gai.GenerativeModel('gemini-1.5-flash')

# Load and extract product names and descriptions from JSON
def load_healthy_products(only_name:bool):
    try:
        data =loadData()
       
        if only_name:
                return {p["name"]: p["description"] for p in data}  # Extract names & descriptions
        else:
                return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data.json: {e}")
        return {}

HEALTHY_PRODUCTS = load_healthy_products(True)

def find_alternative(product_name, product_description):
        
    prompt = f"""
    You are a health-focused assistant. Given a product name: '{product_name}' and its description: '{product_description}', 
    find the best alternative from this list:

    {HEALTHY_PRODUCTS}

    Output only valid JSON without any reasoning or explanations. 

    Use this exact format:
    dont mention "```json"
     {{
        "alternatives": [
        dont mention "```json"
            "// name of the product",       
            "// name of the product"
        ]
    }}
    if no data is similar provide me null
    send me data that i can convert from string to json 
    i dont want any "```" or json and not mentioned like " ```json" only pure json
    """

    # Generate response
    response = client.generate_content(
        prompt,
    
        generation_config={"temperature": 0.0},  # Set to 0 to remove randomness
    )
    # parsed_json = json.loads(response.text)

    if response.text != None:
        model_suggestion= ast.literal_eval(response.text)
        existingdata =load_healthy_products(False)
        
        print(existingdata)
        similar_products = [
            {
                "name": item.get("name", ""),
                "description": item.get("description", ""),
                "company_name":item.get("company_name",""),
                "price":item.get("price",""),
                "qty":item.get("qty",""),
                "health_benefits": item.get("health_benefits", []),
                "common_uses": item.get("common_uses", []),
                "image_url": item.get("image_url", "")
            }
            for item in existingdata  
            if any(suggestion in item.get("name", "") for suggestion in model_suggestion["alternatives"])  # ✅ Filter matching items
        ]
        
        return similar_products



def extract_json_from_response(response):
    try:
        # Ensure response is a dictionary
        if not isinstance(response, dict):
            print("Error: Expected a dictionary.")
            return None

        # Extract the text containing JSON
        raw_text = response.get("candidates", [])[0].get("content", {}).get("parts", [])[0].get("text", "")

        # Ensure it's a valid string
        if not raw_text:
            print("Error: No valid JSON text found.")
            return None

        # Parse JSON
        parsed_json = json.loads(raw_text)
        
        # Convert to formatted JSON string (optional)
        formatted_json = json.dumps(parsed_json, indent=4)
        return formatted_json
    
    except (IndexError, KeyError, json.JSONDecodeError) as e:
        print(f"Error extracting JSON: {e}")
        return None


