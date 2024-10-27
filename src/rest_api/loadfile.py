from flask import jsonify, send_file
from PIL import Image
import io


def upload_file(request):
    # Check if 'file' is in request.files
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    file = request.files['file']  # Access the file
    if file.filename == '':
        return jsonify({'message': 'No file selected'}), 400

    try:
        # Open the file as an image to check if it's valid
        image = Image.open(file)
        image.verify()  # This will raise an exception if it's not an image
        file.seek(0)    # Reset file pointer to start after verification
        return send_file(
            io.BytesIO(file.read()),  # Send the file content as bytes
            mimetype=file.mimetype,
            as_attachment=True,
            download_name=file.filename
        )
    except (IOError, SyntaxError) as e:
        return jsonify({'message': 'File is not a valid image'}), 400
