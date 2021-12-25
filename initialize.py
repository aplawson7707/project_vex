#! /usr/bin/python

import requests

def speak(message):
    message=message
    url = 'http://localhost:12101/api/text-to-speech?play=true'
    headers = {
    	'accept': 'audio/wav',
    	'Content-Type': 'text/plain'
    }
    requests.post(url, headers=headers, data=message)

speak("Good morning. Vocalization protocol is operational. How can I assist you today?")
    