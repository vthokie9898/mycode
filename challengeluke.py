import requests

NAME = 'https://swapi.co/api/people/10/?format=json'

def main():
    r = requests.get(NAME)
    starwars = {}
    print(r.json())
    starwars.update(r.json())
    print(f'{starwars["name"]} is {starwars["hair_color"]}')

main()
