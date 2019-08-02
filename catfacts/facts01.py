#!/usr/bin/env python3
"""Author Trotta:  Cat Facts"""
# imports always go at the top of your code 
import requests

def main():
    """Run time code"""
    # create r, which is our requests object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # the .json method will dump a JSON string into Pythonic data structures.  COOL!
    # This is much easier than using the urllib.request.library
    print( r.json())
main()
