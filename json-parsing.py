from html.entities import name2codepoint
import json
import requests
import pprint
import sys

print('Hello and Welcome to JSON Parsing with Python!\n')

url = 'https://api.wheretheiss.at/v1/satellites/25544'
#params = {"name":"iss"}
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    #pprint.pprint(data)
    name = data['name']
    altitude = data['altitude']
    velocity = data['velocity']
    print(f'{name}\n{altitude}\n{velocity}')
else:
    sys.stderr.write(f'Error: {response.status_code}')
    exit(1)
