import io
from flask import Blueprint, render_template, request, Response, url_for
from gtts import gTTS
from controllers.dyslexia.forms import DyslexiaForm

dyslexia_bp = Blueprint("dyslexia", __name__, template_folder="templates")


def text_to_speech(text, lang="en"):
    """Convert the input text to speech and return as an in-memory audio file."""
    tts = gTTS(text=text, lang=lang, slow=False)
    speech_buffer = io.BytesIO()
    tts.save(speech_buffer)
    speech_buffer.seek(0)
    return speech_buffer


@dyslexia_bp.route("/dyslexia", methods=["GET", "POST"])
def dyslexia():
    form = DyslexiaForm()

    if form.validate_on_submit():
        text = form.big_text.data
        speech_buffer = text_to_speech(text)

        # Serve the generated audio file temporarily via a URL
        audio_url = url_for("dyslexia.speak", _external=True)
        return render_template("dyslexia/dyslexia.html", form=form, audio_url=audio_url)

    return render_template("dyslexia/dyslexia.html", form=form)


@dyslexia_bp.route("/dyslexia/speak", methods=["POST"])
def speak():
    text = request.form.get("text")
    if not text:
        return "No text provided", 400

    speech_buffer = text_to_speech(text)
    return Response(speech_buffer, mimetype="audio/mp3")
