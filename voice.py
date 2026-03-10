import sounddevice as sd
from scipy.io.wavfile import write

def record_audio():

    fs = 44100
    seconds = 5

    print("Recording...")

    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()

    write("input.wav", fs, audio)

    return "input.wav"
