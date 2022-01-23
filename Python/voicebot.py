# import the library
import requests
import speech_recognition as sr  
from gtts import gTTS   
import playsound as ps
from audioplayer import AudioPlayer

sender = input("Selamat datang Artourist . . .\n")
bot_message = ""

while bot_message != "bye":
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:  # mention source it will be either Microphone or audio files.
        recognizer.adjust_for_ambient_noise(mic, 0.2)
        audio = recognizer.listen(mic)  # listen to the source
        print("mendengarkan suara . . .")
        try:
            message = recognizer.recognize_google(audio, language="id")  # use recognizer to convert our audio into text part.
            print(message.lower())
        except:
            print("bisa diulangi lagi?")  # In case of voice not recognized  clearly
    
    if len(message)==0:
        continue
    print("mengirim pesan ...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": message})   
    print("Bot membalas, ", end=' ')
    for i in r.json():
        bot_message = i['text']
        # print(f"{i['text']}")
        print(bot_message)

    tts = gTTS(text=bot_message, lang="id")
    filename = "rekaman.mp3"
    tts.save(filename)
    AudioPlayer(filename).play(block=True)
