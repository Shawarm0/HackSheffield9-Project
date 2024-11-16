from flask import Blueprint, jsonify, redirect, render_template, request, url_for

from controllers.dysgraphia.forms import DysgraphiaForm
from controllers.utils import speech_to_text, send_to_gemini


dysgraphia_bp = Blueprint("dysgraphia", __name__, template_folder="templates")


@dysgraphia_bp.route("/dysgraphia", methods=["GET", "POST"])
def dysgraphia():
    return render_template("dysgraphia/dysgraphia.html")


@dysgraphia_bp.route("/upload_audio", methods=["POST"])
def upload_audio():
    print("Uploading audio")
    if "audio_data" not in request.files:
        return jsonify({"error": "No audio data found"}), 400

    audio_file = request.files["audio_data"]
    audio_file.save("uploaded_audio.wav")  # Save the uploaded audio

    prompt = "You will receive a text containing general ideas expressed by someone who may have dysgraphia. Your task is to interpret the text and generate three main possible written ideas that the person intended to convey, ensuring that the responses are in the first person. Do not summarize their intentions; instead, if the person intended to ask a question, formulate the question as they might have. If they wanted to explain an idea, provide a clear explanation of that idea. The answers must follow this pattern: 'OUTPUT: first answer - explanation of that answer $ OUTPUT: second answer - explanation of that second answer $ OUTPUT: third answer - explanation of that last one.'"

    text = speech_to_text("uploaded_audio.wav")
    with open("dysgraphia_transcript.txt", "w") as f:
        f.write(text)
    output = send_to_gemini(prompt, text)

    answers = output.split("$")
    print(answers)

    return jsonify({"answers": answers})


@dysgraphia_bp.route("/reload_answer", methods=["POST", "GET"])
def reload_answer():
    selected_answer = request.form.get("answer")

    with open("dysgraphia_transcript.txt", "r") as f:
        text = f.read()

    prompt = f"You will receive a text containing general ideas expressed by someone who may have dysgraphia. You are also gonna receive the last generated idea that the user felt that best matches their thoughts. Your task is to interpret the text and generate three main possible written ideas that the person intended to convey, ensuring that the responses are in the first person. Do not summarize their intentions; instead, if the person intended to ask a question, formulate the question as they might have. If they wanted to explain an idea, provide a clear explanation of that idea. The answers must follow this pattern: 'OUTPUT: first answer - explanation of that answer $ OUTPUT: second answer - explanation of that second answer $ OUTPUT: third answer - explanation of that last one.' This is the last generated idea: {selected_answer}"
    output = send_to_gemini(prompt, text)

    return render_template("dysgraphia/try_again.html", answers=output.split("$"))
