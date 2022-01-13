#! /usr/bin/python

import requests

def getCrypto():
    coin='shib'
    url = 'https://cryptfolio.com/api/currencies/'
    response = requests.get(url + coin)
    print(response.text)

getCrypto()