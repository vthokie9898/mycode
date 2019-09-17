#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

LOOKUPAPI = 'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=22611&date=2019-09-17&distance=25&API_KEY=33E42A99-77EA-4C60-8204-97DEE84D15D2'

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    ## set up screen
    print("Weather Forecast")
    print("----------------")

    # display the JSON we were returned as Pythonic datastructures
# loop across the list returned to us
    for x in r.json():
        print(x.get("DateForecast"))
        print("----------")
        print(x.get("ActionDay"))
        if x.get("ActionDay") == False:
            print('Today is a bad day, DO NOT GO OUTSIDE!')

main()
