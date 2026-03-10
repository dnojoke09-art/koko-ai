# main.py
# Railway server entry point

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil

from speech_to_text import transcribe
from ai import ask_ai
from tts import generate_voice

app = FastAPI()

@app.post("/talk")
async def talk(audio: UploadFile = File(...)):

    # Save incoming audio
    with open("input.wav", "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    # Convert speech to text
    user_text = transcribe("input.wav")

    print("User:", user_text)

    # Ask AI
    response = ask_ai(user_text)

    print("Koko:", response)

    # Generate voice
    output_file = generate_voice(response)

    return FileResponse(output_file, media_type="audio/wav")
