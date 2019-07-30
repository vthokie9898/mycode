#!/usr/bin/env python3

# Author:  Mike Trotta
# If statement

hostname = input("What value should we set for hostname? ")

## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("The hostname matches the expected config.")
else:
    print("You are so dumb!  For real!")

# Always print out to the user at the end of a script
print("Exiting script")



