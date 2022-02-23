# -*- coding: utf-8 -*-
"""
MAIN
"""
import json
import requests
from colorama import Fore

def run():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    with open('json-joker.json', 'w') as dataFile:
        json.dump(r.json(), dataFile, indent=4)
    with open('joker.txt', 'w') as dataFile2:
        data = json.loads(r.text)
        str = data["value"]
        dataFile2.write(str)
    print(Fore.BLUE,data)
    return 1
