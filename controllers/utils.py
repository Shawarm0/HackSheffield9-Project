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
import pyttsx3
import io

from pathlib import Path

# Assuming media is the directory path
media = Path("static/images") 


def text_to_speech(text):
    # Initialize the speech engine
    engine = pyttsx3.init()

    # Set properties like rate (speed) and volume (0.0 to 1.0)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Split the input text into lines
    lines = text.splitlines()

    # Convert each line to speech
    for line in lines:
        if line.strip():  # Skip empty lines
            engine.say(line)
            engine.runAndWait() 


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


def image_to_gemini():
    genai.configure(api_key="AIzaSyBK7p-x-WsOzMTWXEfEOoSeRF-CWZ98JGU")
    myfile = genai.upload_file(media / "Figure.png")

    model = genai.GenerativeModel("gemini-1.5-flash")
    result = model.generate_content(
    [myfile, "\n\n", "The picture is from a dyslexic person can you try your best to decypher it. If there are some words that are indecypherable can you use context clues to fill in the gaps. In your reply only include the text you think is displayed. Nothing else."]
    )
    return result.text
       
