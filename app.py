import sys
import os
from io import BytesIO

from functools import wraps
from flask import Flask, request, jsonify
from PIL import Image
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from src.gen.global_model import genCall
from src.gen.local_model import find_alternative
from src.gen.image_text import process_image
from src.routes.rest_urls import Prompt_Url
from src.gen.compare import comapare_process_image



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



# ratio
#//////////////////////////////////////////////////



@app.route(Prompt_Url.ratio_prompt, methods=['POST'])
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



#health 
#/////////////////////////////////////////////////


@app.route(Prompt_Url.health_prompt, methods=['POST'])
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



#conclusion
#////////////////////////////////////////////////



@app.route(Prompt_Url.conclusion_prompt, methods=['POST'])
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


# compare products

@app.route(Prompt_Url.com_compare_product, methods=['POST'])
def compare_product_log():
    try:
        if 'image1' not in request.files:
            return jsonify({"error": "No image1 file found in the request"}), 400
        if 'image2' not in request.files:
            return jsonify({"error": "No image2s file found in the request"}), 400

        image_file1 = request.files['image1']

        image_file2= request.files['image2']
        image1 = Image.open(BytesIO(image_file1.read()))
        image2 =Image.open(BytesIO(image_file2.read()))
        image_to_text_data = comapare_process_image(image1, image2)
        return jsonify(image_to_text_data)
    
    except ValueError as ve:
        return jsonify({'errorstr': str(ve)}), 400  # Return the error mes
    except Exception as e:
        return jsonify({'error': str(e)})



@app.route(Prompt_Url.alternativeSuggestion, methods=["POST"])
def suggest_product():
    try:
        data = request.json
        if not data or "product" not in data or "data" not in data:
            return jsonify({"error": "Missing 'product' or 'data' field"}), 400

        product_name = data["product"].lower() if isinstance(data["product"], str) else ""
        product_description = data["data"].lower() if isinstance(data["data"], str) else ""
        alternative = find_alternative(product_name, product_description)

        return jsonify({"alternative": alternative})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
    

@app.route("/api/generateAlternative", methods=["POST"])
def generate():
 try:
    data =request.json
    if not data or "product" not in data or "data" not in data:
            return jsonify({"error": "Missing 'product' or 'data' field"}), 400

    print(data["product"])
    response= genCall(data["product"])

    return response

 except Exception as e:
    print(f"Error: {e}")
    return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)


