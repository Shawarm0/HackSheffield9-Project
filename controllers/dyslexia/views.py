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
            "Can you take the text below and create a big story from it as detailed as possible",
            f"{text}"
        )

        # Start the text-to-speech process in a separate thread
        tts_thread = threading.Thread(target=handle_text_to_speech, args=(processed_text,))
        tts_thread.start()

        # Return the processed text as JSON
        return jsonify({"processed_text": processed_text})

    # Render the default template for GET requests
    return render_template("dyslexia/dyslexia.html")


