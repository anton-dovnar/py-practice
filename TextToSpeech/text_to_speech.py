from gtts import gTTS

with open('article.txt') as f:
    text_to_speech = gTTS(text=f.read(), lang='en', slow=False)
    text_to_speech.save("audio-text.mp3")

print("Audio Saved")
