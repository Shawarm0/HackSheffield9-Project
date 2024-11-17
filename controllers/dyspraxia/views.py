from flask import Blueprint, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from controllers.utils import image_to_gemini

dyspraxia_bp = Blueprint("dyspraxia", __name__, template_folder="templates")

UPLOAD_FOLDER = "static/images"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

# Ensure the 'images' folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@dyspraxia_bp.route("/dyspraxia", methods=["GET", "POST"])
def dyspraxia():
    if request.method == "POST":
        if "file" not in request.files:
            return jsonify({"message": "No file part"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"message": "No selected file"}), 400

        if file and allowed_file(file.filename):
            # Secure the filename and save the file
            file_path = os.path.join(UPLOAD_FOLDER, "Figure.png")
            file.save(file_path)

            # Process the image using image_to_gemini, which returns a string
            gemini_text = image_to_gemini()
            gemini_text = gemini_text.replace("\n", " ")
            # Generate image URL to return to the front-end
            image_url = f"static/{UPLOAD_FOLDER}/Figure.png"
            print(image_url)

            # Return success response with both image URL and processed text
            return (
                jsonify(
                    {
                        "message": "File uploaded successfully!",
                        "image_url": image_url,
                        "gemini_text": gemini_text,
                    }
                ),
                200,
            )
        else:
            return (
                jsonify(
                    {
                        "message": "Invalid file format. Only png, jpg, jpeg, and gif are allowed."
                    }
                ),
                400,
            )

    return render_template("dyspraxia/dyspraxia.html")
