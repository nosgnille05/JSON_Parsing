import json
from statistics import mean
import requests
import pprint
import sys
import time

def km_to_mile(kilometers: float) -> float:
    return kilometers * 0.62137

def avg_velocity(url) -> float:
    print('Starting Avg Velocity Calculator . . .\nGathering Data (approx. 10 sec) . . .')
    velocities = []
    for x in range (0, 5):
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            velocity = data['velocity']
            velocities.append(velocity)
        else:
            sys.stderr.write(f'Error: {response.status_code}')
            exit(1)
        time.sleep(2)
    return mean(velocities)

if __name__ == "__main__":
    print('Hello and Welcome to JSON Parsing with Python!\n')

    url = 'https://api.wheretheiss.at/v1/satellites/25544'
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        pprint.pprint(data)
        name = data['name']
        timestamp = data['timestamp']
        altitude = data['altitude']
        velocity = data['velocity']
        print(f'\nInformation in (km) for the {name}\n        time:    {timestamp}\n    Altitude: {altitude} (km)\n    Velocity: {velocity} (km/hr)\n')
        print('Lets convert to miles!\n')
        altitude = km_to_mile(altitude)
        velocity = km_to_mile(velocity)
        print(f'Information in (mi) for the {name}\n        time:    {timestamp}\n    Altitude: {altitude} (mi)\n    Velocity: {velocity} (mi/hr)\n')
    else:
        sys.stderr.write(f'Error: {response.status_code}')
        exit(1)

    avg_velocity = avg_velocity(url)
    print(f'ISS Average Velocity (km/hr): {avg_velocity}')
    print(f'ISS Average Velocity (mi/hr): {km_to_mile(avg_velocity)}')
