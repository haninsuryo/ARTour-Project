import playsound as ps
from gtts import gTTS
from audioplayer import AudioPlayer

def bilang(text):
  tts = gTTS(text=text, lang="id")
  filename = "rekaman.mp3"
  tts.save(filename)
  AudioPlayer(filename).play(block=True)

mytext = 'Ada yang bisa dibantu?'
bilang(mytext)