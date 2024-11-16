from flask import Blueprint, render_template, request
from controllers.utils import send_to_gemini, text_to_speech
import threading

dyslexia_bp = Blueprint("dyslexia", __name__, template_folder="templates")

def handle_text_to_speech(text):
    text_to_speech(text)


@dyslexia_bp.route("/dyslexia", methods=["GET", "POST"])
def dyslexia():
    if request.method == "POST":
        text = request.form.get("text")# Retrieve the text from the form
        processed_text = send_to_gemini("Can you take the text below and create a big story from it as detailed as possible", f"{text}") 
        
        tts_thread = threading.Thread(target=handle_text_to_speech, args=(processed_text,))
        tts_thread.start()
        
        return render_template("dyslexia/dyslexia.html", text=processed_text)  # Acknowledge the request

    # Default response for GET requests
    return render_template("dyslexia/dyslexia.html")

