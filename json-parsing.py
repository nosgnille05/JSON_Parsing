import json
import requests
import pprint
import sys
import time

def km_to_mile(kilometers: float) -> float:
    return kilometers * 0.62137

def velocity_descrepancy(url) -> float:
    print('Starting Descrepancy Calculator . . . (approx. 10 sec)')
    for x in range (0, 5):
        #do stuff
        print(f'x: {x}')
        x += 1
        time.sleep(2)
    """
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        #pprint.pprint(data)
        name = data['name']
        timestamp = data['timestampstamp']
        altitude = data['altitude']
    else:
        sys.stderr.write(f'Error: {response.status_code}')
        exit(1)
    """


print('Hello from json-parsing.py')

if __name__ == "__main__":
    print('Hello and Welcome to JSON Parsing with Python!\n')

    url = 'https://api.wheretheiss.at/v1/satellites/25544'
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        #pprint.pprint(data)
        name = data['name']
        timestamp = data['timestamp']
        altitude = data['altitude']
        velocity = data['velocity']
        print(f'Information in (km) for the {name}\n        time:    {timestamp}\n    Altitude: {altitude} (km)\n    Velocity: {velocity} (km/hr)\n')
        print('Lets convert to miles!\n')
        altitude = km_to_mile(altitude)
        velocity = km_to_mile(velocity)
        print(f'Information in (miles) for the {name}\n        time:    {timestamp}\n    Altitude: {altitude} (miles)\n    Velocity: {velocity} (miles/hr)\n')
    else:
        sys.stderr.write(f'Error: {response.status_code}')
        exit(1)

    velocity_descrepancy(url)
