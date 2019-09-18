import requests
import argparse


NAME = 'https://swapi.co/api/people/10/?format=json'

def main():
    r = requests.get(f'https://swapi.co/api/people/1/?format=json')
    data = r.json()
    print(f'{data["name"]} is {data["hair_color"]}')


    parser = argparse.ArgumentParser(description="Add a gender attribute")
    parser.add_argument('-att', metavar='attribute', type=str, help="Ask for any attribute")
    args = parser.parse_args()
    force_json = requests.get(NAME).json()
    keys = list(force_json.keys())

    print(f'Name - {force_json.get("name")}\nHair Color - {force_json.get("hair_color")}\nOptional Attribute:{args.att} - {force_json.get(args.att)}')
    print('------------------------------------------------------------------------------')
    if args.keys:
        print("Try running the script again.This time choose any attribute from the list and pass them as argument with -att")
        for key in keys:
            print(key)

main()
