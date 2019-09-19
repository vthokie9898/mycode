#!/usr/bin/env python3

from flask import Flask #, jsonify
import requests

app = Flask(__name__)

@app.route('/planets')
def index():
    planets = {}    
    for i in range(1,11):
    
        r = requests.get(f'https://swapi.co/api/planets/{i}/?format=json')
        data = r.json()
        #print(data)
        planets.update({data['name']: data['climate']})

    return planets
    # return jsonify(planets)

if __name__ == "__main__":
    app.run(port=5006)
