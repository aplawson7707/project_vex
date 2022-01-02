#! /usr/bin/python

import requests
import random

greetings = [
    "Hello ",
    "Good day",
    "Greetings ",
    "Good to see you ",
    "Pleasure to see you ",
    "It's very good to see you ",
    "Hello there ",
    "How do you do "
]

random_greeting = random.randrange(len(greetings))

def speak(message):
    message=message
    url = 'http://localhost:12101/api/text-to-speech?play=true'
    headers = {
    	'accept': 'audio/wav',
    	'Content-Type': 'text/plain'
    }
    requests.post(url, headers=headers, data=message)

# speak("Good morning. Vocalization protocol is operational. How can I assist you today?")
speak(greetings[random_greeting] + "Josiah")