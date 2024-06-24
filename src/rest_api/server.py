import sys
import os
from flask import Flask, request, jsonify

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from image_to_text.image_text import process_image

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/initialPrompt', methods=['POST'])
def upload_initial_image():
    try:
        data = request.json
        image_to_text_data = process_image(data['data']['imageUrl'], "initial_data_text")
        return jsonify(image_to_text_data)
    except Exception as e:
        return jsonify({'error': str(e)})



@app.route('/ratioPrompt', methods=['POST'])
def upload_ratio_image():
    try:
        data = request.json
        image_to_text_data = process_image(data['data']['imageUrl'], "ratio_specified_text")
        return jsonify(image_to_text_data)
    except Exception as e:
        return jsonify({'error': str(e)})
    



@app.route('/healthPrompt', methods=['POST'])
def upload_health_image():
    try:
        data = request.json
        image_to_text_data = process_image(data['data']['imageUrl'], "health_consideration_text")
        return jsonify(image_to_text_data)
    except Exception as e:
        return jsonify({'error': str(e)})
    


@app.route('/conclusionPrompt', methods=['POST'])
def upload_conclusion_image():
    try:
        data = request.json
        image_to_text_data = process_image(data['data']['imageUrl'], "conclusion_text")
        return jsonify(image_to_text_data)
    except Exception as e:
        return jsonify({'error': str(e)})     
if __name__ == '__main__':
    app.run()
