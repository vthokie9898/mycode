#!/usr/bin/env python3
## Create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## Display file to the screen - .read()
configblog = configfile.read()

## Break configblog across line boundaries (strip out /n)
configlist = configblog.splitlines()

## display list with no "\n"
print(configlist)



## Always close your file
configfile.close()
