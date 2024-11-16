from flask import Blueprint, render_template, request, jsonify
from controllers.utils import image_to_gemini
import os

dyspraxia_bp = Blueprint("dyspraxia", __name__, template_folder="templates")

# Ensure the 'images' folder exists
UPLOAD_FOLDER = 'images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@dyspraxia_bp.route("/dyspraxia", methods=["GET", "POST"])
def dyspraxia():
    if request.method == "POST":
        if 'file' not in request.files:
            return jsonify({"message": "No file part"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"message": "No selected file"}), 400

        # Save the file to the 'images/' folder
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        image_to_gemini(file.filename)
        return jsonify({"message": "File uploaded successfully!"}), 200

    return render_template("dyspraxia/dyspraxia.html")

