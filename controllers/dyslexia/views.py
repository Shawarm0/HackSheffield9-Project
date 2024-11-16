from flask import Blueprint, render_template, request
from controllers.utils import send_to_gemini, text_to_speech


dyslexia_bp = Blueprint("dyslexia", __name__, template_folder="templates")

@dyslexia_bp.route("/dyslexia", methods=["GET", "POST"])
def dyslexia():
    if request.method == "POST":
        text = request.form.get("text")# Retrieve the text from the form
        processed_text = send_to_gemini("Can you take the text below and create a big story from it as detailed as possible", f"{text}") 

        print(text)  # Print the text to the console
        return processed_text  # Acknowledge the request

    # Default response for GET requests
    return render_template("dyslexia/dyslexia.html")

