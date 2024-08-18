import sys
import os
import jwt
import datetime
from functools import wraps
from flask import Flask, request, jsonify, abort




sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from src.rest_api.errors.error_text import ErrorForms, ErrorNumber
from src.prompt.prompt_url import Prompt_Url
from src.image_to_text.image_text import process_image
from src.rest_api.mongo import validate_user  

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("APP_CONFIG_KEY")

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

@app.route(Prompt_Url.login, methods=['POST'])
def login():
   
    auth = request.json
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

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route(Prompt_Url.check_Server, methods=['GET'])
def onLoad():
    return 'Server is working perfectly!'

@app.route(Prompt_Url.initial_prompt, methods=['POST'])
@token_required
def upload_initial_image(current_user):
    try:
        data = request.json
        image_to_text_data = process_image(data['data']['imageUrl'], "initial_data_text")
        return jsonify(image_to_text_data)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route(Prompt_Url.ratio_prompt, methods=['POST'])
@token_required
def upload_ratio_image(current_user):
    try:
        data = request.json
        image_to_text_data = process_image(data['data']['imageUrl'], "ratio_specified_text")
        return jsonify(image_to_text_data)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route(Prompt_Url.health_prompt, methods=['POST'])
@token_required
def upload_health_image(current_user):
    try:
        data = request.json
        image_to_text_data = process_image(data['data']['imageUrl'], "health_consideration_text")
        return jsonify(image_to_text_data)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route(Prompt_Url.conclusion_prompt, methods=['POST'])
@token_required
def upload_conclusion_image(current_user):
    try:
        data = request.json
        image_to_text_data = process_image(data['data']['imageUrl'], "conclusion_text")
        return jsonify(image_to_text_data)
    except Exception as e:
        return jsonify({'error': str(e)}) 

if __name__ == '__main__':
    app.run()
