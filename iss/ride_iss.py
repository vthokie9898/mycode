#!/usr/bin/env python3
"""lab from Chad"""
import urllib.request
import json
## define url
MAJORTOM = 'http://api.open-notify.org/astros.json'
def main():
    """main function"""
    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)
    ## put fileobject into helmet
    helmet = groundctrl.read()
    ## decode json to python data source
    helmetson = json.loads(helmet.decode('utf-8'))
    ## display our pythonic data
    print("\n\nConverted python data")
    print(helmetson)
    print("\n\nPeople in space: ", helmetson['number'])
    people = helmetson['people']
    for x in people:
        print(x['name'] + ' is on the ' + x['craft'])
    print("\n\n\n")
    for x in people:
        print(f"{x['name']} is on the {x['craft']}")
main()
