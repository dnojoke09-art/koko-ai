import requests
import pygame
import customtkinter as ctk

from voice import record_audio

SERVER = "https://YOUR-RAILWAY-URL/talk"

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Koko AI")
app.geometry("400x300")

label = ctk.CTkLabel(app,text="Koko AI Companion")
label.pack(pady=20)

output = ctk.CTkTextbox(app,height=100,width=300)
output.pack(pady=10)

def talk():

    output.insert("end","Recording...\n")

    audio_file = record_audio()

    files = {"audio": open(audio_file,"rb")}

    r = requests.post(SERVER,files=files)

    with open("response.mp3","wb") as f:
        f.write(r.content)

    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()

    output.insert("end","Koko responded\n")

button = ctk.CTkButton(app,text="Talk to Koko",command=talk)
button.pack(pady=20)

app.mainloop()
