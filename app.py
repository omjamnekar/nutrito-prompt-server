import sys
import os
from io import BytesIO

import datetime
from functools import wraps
from flask import Flask, request, jsonify
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from src.database.errors.error_text import ErrorForms, ErrorNumber
from src.image_to_text.image_text import process_image
from src.database.mongo import validate_user  
from src.routes.rest_urls import Prompt_Url

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("APP_CONFIG_KEY")




@app.route('/')
def hello():
    return 'Hello, World!'

@app.route(Prompt_Url.check_Server, methods=['GET'])
def onLoad():
    return 'Server is working perfectly!'



#  //nutrition 
#/////////////////////////////////////////////////////////////////

@app.route(Prompt_Url.initial_prompt, methods=['POST'])
# @token_required
def upload_initial_image():
    
    try:
           
        if 'image' not in request.files:
            return jsonify({"error": "No image file found in the request"}), 400

        image_file = request.files['image']
        image = Image.open(BytesIO(image_file.read()))

    
        image_to_text_data = process_image(image, "initial_data_text")
        return jsonify(image_to_text_data)
    except ValueError as ve:
        return jsonify({'errorstr': str(ve)}), 400  # Return the error message with a 400 status
    except Exception as e:
        return jsonify({'errorstr': 'An unexpected error occurred: ' + str(e)}), 500  # Handle unexpected errors







@app.route(Prompt_Url.ratio_prompt, methods=['POST'])
# @token_required
def upload_ratio_image():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file found in the request"}), 400

        image_file = request.files['image']
        image = Image.open(BytesIO(image_file.read()))

        
        image_to_text_data = process_image(image, "ratio_specified_text")
        return jsonify(image_to_text_data)
    except ValueError as ve:
        return jsonify({'errorstr': str(ve)}), 400  # Return the error mes
    except Exception as e:
        return jsonify({'error': str(e)})






@app.route(Prompt_Url.health_prompt, methods=['POST'])
# @token_required
def upload_health_image():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file found in the request"}), 400

        image_file = request.files['image']
        image = Image.open(BytesIO(image_file.read()))
        image_to_text_data = process_image(image, "health_consideration_text")
        return jsonify(image_to_text_data)
    

    except ValueError as ve:
        return jsonify({'errorstr': str(ve)}), 400  # Return the error mes
    except Exception as e:
        return jsonify({'error': str(e)})







@app.route(Prompt_Url.conclusion_prompt, methods=['POST'])
# @token_required
def upload_conclusion_image():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file found in the request"}), 400

        image_file = request.files['image']
        image = Image.open(BytesIO(image_file.read()))
        image_to_text_data = process_image(image, "conclusion_text")
        return jsonify(image_to_text_data)
    
    except ValueError as ve:
        return jsonify({'errorstr': str(ve)}), 400  # Return the error mes
    except Exception as e:
        return jsonify({'error': str(e)})




#  //compare feature 
#/////////////////////////////////////////////////////////////////




if __name__ == '__main__':
    app.run(debug=True)


