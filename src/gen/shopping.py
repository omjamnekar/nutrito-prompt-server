
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.util.shopping import produceNames
import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])



# === 4. Define a function to query Gemini with context ===
def get_shopping_list(user_need)->str:
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    You are a health-based shopping assistant. A user will describe what they need for their health (like digestion, immunity, etc.).
    Based on the benefits of the available products listed below, return only a list of product names (fruits and vegetables) that match their request.

    ### Product List:
    {produceNames}

    ### User Request:
    {user_need}

    ### Shopping List (only product names in json no other text before and after it):
    {{
        "message": "provide message for your query and or any suggestion for user any 6 to 8",
        "productname": ["provide data over here"]
    }}

    dont put ```json and ``` anywhere in full response
    """

    response = model.generate_content(prompt)
    return response.text.strip()


  