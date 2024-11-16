from flask import Blueprint, render_template, request, jsonify
from controllers.utils import send_to_gemini, text_to_speech
import threading

dyslexia_bp = Blueprint("dyslexia", __name__, template_folder="templates")

def handle_text_to_speech(text):
    text_to_speech(text)

@dyslexia_bp.route("/dyslexia", methods=["GET", "POST"])
def dyslexia():
    if request.method == "POST":
        data = request.get_json()  # Get JSON data from the request
        text = data.get("text")  # Extract the 'text' key

        # Process the text
        processed_text = send_to_gemini(
            "Can you get the text below and make it more concise and shorter, explain what it says to someone that may have dyslexia or other learning disabilities. Make sure that the return text has line breaks after each clearly explained point. DO NOT use any special characters other than punctuation",
            f"{text}"
        )

        # Start the text-to-speech process in a separate thread
        tts_thread = threading.Thread(target=handle_text_to_speech, args=(processed_text,))
        tts_thread.start()

        # Return the processed text as JSON
        return jsonify({"processed_text": processed_text})

    # Render the default template for GET requests
    return render_template("dyslexia/dyslexia.html")

