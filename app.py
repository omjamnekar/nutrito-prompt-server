import sys
import os
import jwt
from PIL import Image
from io import BytesIO

import datetime
from functools import wraps
from flask import Flask, request, jsonify
from PIL import Image





sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from src.rest_api.errors.error_text import ErrorForms, ErrorNumber
from src.image_to_text.image_text import process_image
from src.rest_api.mongo import validate_user  
from src.network.rest_urls import Prompt_Url

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("APP_CONFIG_KEY")


from flask import request, jsonify
from PIL import Image





def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': ErrorForms.token_missing}), ErrorNumber.forbidden

        try:
            token = token.replace("Bearer ", "")
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['user']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), ErrorNumber.forbidden
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), ErrorNumber.forbidden

        return f(current_user, *args, **kwargs)
    
    return decorated





@app.route('/')
def hello():
    return 'Hello, World!'

@app.route(Prompt_Url.check_Server, methods=['GET'])
def onLoad():
    return 'Server is working perfectly!'


@app.route(Prompt_Url.login, methods=['POST'])
def login():
    auth =request.json
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': ErrorForms.could_not_verify, 'WWW-Authenticate': ErrorForms.login_required}), ErrorNumber.unauthorized

    _username = auth.get('username')
    _password = auth.get('password')
   
    if validate_user(_username, _password):
        
        token = jwt.encode({
            'user': _username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})
    
    return jsonify({'message': ErrorForms.envalid_credential}), ErrorNumber.unauthorized






@app.route(Prompt_Url.initial_prompt, methods=['POST'])
@token_required
def upload_initial_image(current_user):
    
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
@token_required
def upload_ratio_image(current_user):
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
@token_required
def upload_health_image(current_user):
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
@token_required
def upload_conclusion_image(current_user):
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





if __name__ == '__main__':

    app.run()



