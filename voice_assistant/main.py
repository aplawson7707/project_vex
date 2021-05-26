import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en", tld="co.za")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

speak("Good afternoon sir. All systems are nominal and I am ready to help")

