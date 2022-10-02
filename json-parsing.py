import json
import requests

print('Hello and Welcome to JSON Parsing with Python!\n')

url = requests.get('https://api.wheretheiss.at/v1/satellites/25544')

print(url.json())
