from gtts import gTTS

def create_voice(text):
    tts = gTTS(text=text, lang="en")
    tts.save("voice.mp3")
    return "voice.mp3"
