# General methods 
from flask import Flask, request, Response
from gtts import gTTS
import os
import io 

from flask import Blueprint, render_template


def text_to_speech(text, lang='en'):
    """Convert the input text to speech and return as an in-memory audio file."""
    tts = gTTS(text=text, lang=lang, slow=False)
    # Create an in-memory buffer to store the speech audio
    speech_buffer = io.BytesIO()
    tts.save(speech_buffer)
    speech_buffer.seek(0)  # Move to the beginning of the buffer
    return speech_buffer


def speak():
    """Receive text, convert it to speech, and return the audio file in-memory for playback."""
    text = request.form.get('text')  # Get the text from the POST request
    if not text:
        return "No text provided", 400  # Return an error if no text is provided

    # Generate speech from text and get the in-memory file
    speech_buffer = text_to_speech(text)

    # Send the generated speech as an audio file in-memory for playback
    return Response(speech_buffer, mimetype='audio/mp3')
