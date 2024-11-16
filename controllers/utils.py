# General methods
from flask import Flask, request, Response
from gtts import gTTS
import os
import io
import google.generativeai as genai
import whisper

import sounddevice as sd
from scipy.io.wavfile import write


from flask import Blueprint, render_template
import pyttestx3
import io


def text_to_speech(text):
    # Initialize the speech engine
    engine = pyttsx3.init()

    # Set properties like rate (speed) and volume (0.0 to 1.0)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Convert the input text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

def speak():
    """Receive text, convert it to speech, and return the audio file in-memory for playback."""
    text = request.form.get("text")  # Get the text from the POST request
    if not text:
        return "No text provided", 400  # Return an error if no text is provided

    # Generate speech from text and get the in-memory file
    speech_buffer = text_to_speech(text)

    # Send the generated speech as an audio file in-memory for playback
    return Response(speech_buffer, mimetype="audio/mp3")


def speech_to_text(file_name: str):
    model = whisper.load_model("medium.en")
    result = model.transcribe(file_name)

    # If result['text'] is a list, join its elements into a single string
    if isinstance(result["text"], list):
        return " ".join(result["text"])  # Concatenate the list into a single string
    return result["text"]  # If it's already a string, return it directly


def send_to_gemini(prompt: str, text: str):
    genai.configure(api_key="AIzaSyBK7p-x-WsOzMTWXEfEOoSeRF-CWZ98JGU")
    model = genai.GenerativeModel("gemini-1.5-flash-8b")
    response = model.generate_content(f"{prompt} \n \n {text}")
    return response.text


def record_audio(filename="output.wav", duration=10, sample_rate=44100):
    """
    Records audio from the microphone and saves it to a WAV file.

    Args:
        filename (str): The name of the file to save the recording.
        duration (int): Duration of the recording in seconds.
        sample_rate (int): Sampling rate in Hz (default: 44100).
    """
    print("Recording... Speak into the microphone.")
    try:
        # Record audio
        audio = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16",
        )
        sd.wait()  # Wait until recording is finished
        print("Recording finished. Saving to file...")

        # Save the audio to a WAV file
        write(filename, sample_rate, audio)
        print(f"Recording saved to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
