from gtts import gTTS

def generate_voice(text):

    file = "response.mp3"

    tts = gTTS(text=text, lang="en")

    tts.save(file)

    return file
