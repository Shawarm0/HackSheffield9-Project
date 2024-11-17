from flask import Blueprint, render_template, request, jsonify
from controllers.utils import send_to_gemini, text_to_speech
import threading

dyslexia_bp = Blueprint("dyslexia", __name__, template_folder="templates")

# Global variable to control TTS
stop_tts_flag = threading.Event()


def handle_text_to_speech(text):
    global stop_tts_flag
    stop_tts_flag.clear()  # Reset the flag
    for chunk in text.splitlines():  # Assume text_to_speech processes text in chunks
        if stop_tts_flag.is_set():
            break
        text_to_speech(chunk)  # Call the TTS function for each chunk
        # Add a small delay if needed to simulate processing
    return


@dyslexia_bp.route("/dyslexia", methods=["GET", "POST"])
def dyslexia():
    if request.method == "POST":
        data = request.get_json()  # Get JSON data from the request
        text = data.get("text")  # Extract the 'text' key

        # Process the text
        processed_text = send_to_gemini(
            "Can you get the text below and make it more concise and shorter, explain what it says to someone that may have dyslexia or other learning disabilities. Make sure that the return text has line breaks after each clearly explained point. DO NOT use any special characters other than punctuation.",
            f"{text}",
        )

        # Start the text-to-speech process in a separate thread
        tts_thread = threading.Thread(
            target=handle_text_to_speech, args=(processed_text,)
        )
        tts_thread.start()

        # Return the processed text as JSON
        return jsonify({"processed_text": processed_text})

    # Render the default template for GET requests
    return render_template("dyslexia/dyslexia.html")


@dyslexia_bp.route("/dyslexia/quit", methods=["POST"])
def quit_tts():
    global stop_tts_flag
    stop_tts_flag.set()  # Signal the TTS process to stop
    return jsonify({"success": True})
