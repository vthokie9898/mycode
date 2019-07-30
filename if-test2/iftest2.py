#!/usr/bin/env python3
#Author:  Trotta

ipchk = input("Apply an IP address: ") # This line now prompts the user for input

if ipchk == "192.168.70.1": # if any data is provided, this will test true
    print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")

elif ipchk: # if any data is provided, this will test true
    print("Looks like the IP address was set: " + ipchk)

else: # If data is not provided
    print("Bro, are you even paying attention?")


print("The script has completed!")

