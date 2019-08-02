#!/usr/bin/env python3
"""Author Trotta:  Cat Facts"""
# imports always go at the top of your code
import requests
def main():
    """Run time code"""
    # create r, which is our requests object
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    ## catfact is our iterable -- that just means it will take on the values found with
    ## r.json()['all'], one after the next -- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with the text"
    for catfact in r.json()['all']:
        print(catfact.get("text"))  # the .get() method returns NONE if key not found
main()
