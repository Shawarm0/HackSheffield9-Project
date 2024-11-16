# General methods 
from flask import Flask, request, Response
from gtts import gTTS
import os
import io 
import google.generativeai as genai
import whisper


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


def speech_to_text(file_name: str):
    model = whisper.load_model("medium.en")
    result = model.transcribe(file_name)
    
    # If result['text'] is a list, join its elements into a single string
    if isinstance(result['text'], list):
        return " ".join(result['text'])  # Concatenate the list into a single string
    return result['text']  # If it's already a string, return it directly


def send_to_gemini(prompt:str, text: str):
    genai.configure(api_key="AIzaSyBK7p-x-WsOzMTWXEfEOoSeRF-CWZ98JGU")
    model = genai.GenerativeModel("gemini-1.5-flash-8b")
    response = model.generate_content(f"{prompt} \n \n {text}")
    return response.text


