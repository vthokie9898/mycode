#!/usr/bin/env python3

def main():
    cars = {'number': 3, 
            'vehicles': [{'brand': 'Kia', 'model': 'Soul'},
                        {'brand': 'Tesla', 'model': 'ModelS'},
                        {'brand': 'Chevy', 'model': 'Tahoe'}],
            'colors': ['red', 'white', 'blue']}

    print(f"I have {cars.get('number')} cars, a {cars['colors'][0]} {cars['vehicles'][0]['brand']} {cars['vehicles'][0]['model']}, a {cars['colors'][1]} {cars['vehicles'][1]['brand']} {cars['vehicles'][1]['model']}, and a {cars['colors'][2]} {cars['vehicles'][2]['brand']} {cars['vehicles'][2]['model']}.")

    print('***************************************************************')

    c = cars['colors']
    v = cars['vehicles']
    m = 'model'
    b = 'brand'

    print(f"I have {cars['number']} cars, a {c[0]} {v[0][b]} {v[0][m]}, a {c[0]} {v[1][b]} {v[1][m]}, and a {c[2]} {v[2][b]} {v[2][m]}.")


main()
