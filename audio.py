"""
Convert text into audio file.
"""
# pip install playsound
from playsound import playsound
# pip install gtts
from gtts import gTTS

audio_file = "speech.mp3"

file = open("IMM_big_sentences 5acee00b-1c6c-496c-96b6-4d0e11c73db2.txt", "r").read().replace("\n", " ")

language = "es"
region = "es"
speech = gTTS(text=str(file), lang=language, tld=region, slow=True)

speech.save(audio_file)
#playsound(audio_file)

from pydub import AudioSegment
sound1 = AudioSegment.from_file("base.mp3", format="mp3")
sound2 = AudioSegment.from_file("speech.mp3", format="mp3")

# sound1 6 dB louder
#louder = (sound2 + 6)

# sound1, with sound2 appended (use louder instead of sound1 to append the louder version)
#combined = sound1 + louder

# Overlay sound2 over sound1 at position 0  (use louder instead of sound1 to use the louder version)
#overlay = sound1.overlay(sound2, position=0)
overlay = sound1.overlay(sound2, position=0.1*len(sound1))

overlay = overlay.overlay(sound2, position=0.35*len(sound1))
overlay = overlay.overlay(sound2, position=0.70*len(sound1))

# simple export
file_handle = overlay.export("hit.ogg", format="ogg")