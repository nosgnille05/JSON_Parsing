from html.entities import name2codepoint
import json
import requests
import pprint
import sys

def km_to_mile(kilometers: float) -> float:
    return kilometers * 0.62137

print('Hello and Welcome to JSON Parsing with Python!\n')

url = 'https://api.wheretheiss.at/v1/satellites/25544'
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    #pprint.pprint(data)
    name = data['name']
    time = data['timestamp']
    altitude = data['altitude']
    velocity = data['velocity']
    print(f'Information in (km) for the {name}\n        Time:    {time}\n    Altitude: {altitude} (km)\n    Velocity: {velocity} (km/hr)\n')
    print('Lets convert to miles!\n')
    altitude = km_to_mile(altitude)
    velocity = km_to_mile(velocity)
    print(f'Information in (miles) for the {name}\n        Time:    {time}\n    Altitude: {altitude} (miles)\n    Velocity: {velocity} (miles/hr)\n')
else:
    sys.stderr.write(f'Error: {response.status_code}')
    exit(1)
