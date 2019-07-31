#!/usr/bin/env python3
# This library allows us to generate uuid values.
import uuid

howmany = input("How many UUIDs should be generated? ")
if howmany.isnumeric():
    print("Generating UUIDs...")
    for rando in range(int(howmany)):
        print( uuid.uuid4())

else:
    print("Must be a number, try again")


