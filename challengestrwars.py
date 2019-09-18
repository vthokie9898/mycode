import requests
import argparse

for i in range(1, 10):
    r = requests.get(f'https://swapi.co/api/people/{i}/?format=json')
    data = r.json()
    #print(data)
    print(f"{data['name']} is {data['hair_color']}")


