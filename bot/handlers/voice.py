from gtts import gTTS

def create_voice(text):
    tts = gTTS(text=text, lang="en")
    path = "voice.mp3"
    tts.save(path)
    return path
