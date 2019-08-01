#!/usr/bin/env python3
import netifaces
print(netifaces.interfaces())
for i in netifaces.interfaces():
     print("\n************Details of Interface - " + i + " ************")
     try:
         print('MAC: ', end="") # This print statement will alwyas print MAC without an end of line
         print(netifaces.ifaddresses(i) [netifaces.AF_LINK] [0] ['addr']) # prints the MAC address
         print('IP: ', end="") # This print statement will always print IP without an end of line
         print(netifaces.ifaddresses(i) [netifaces.AF_INET] [0] ['addr']) # prints the IP address
     except:
         print('Could not collect adapter information') # Print an error message

print("\n" * 5)
x = input("What adapter do you want the IP address of? ")
def IP(interface):
    try:
        print('IP: ', end="") # This print statement will always print IP without an end of line
        print(netifaces.ifaddresses(interface) [netifaces.AF_INET] [0] ['addr']) # prints the IP address
    except:
        print('Could not collect adapter information') # Print an error message

IP(x)

print("\n" * 5)
y = input("What adapter do you want the MAC address of? ")
def MAC(address):
    try:
        print('MAC: ', end="") # This print statement will always print IP without an end of line
        print(netifaces.ifaddresses(address) [netifaces.AF_LINK] [0] ['addr']) # prints the IP address
    except:
        print('Could not collect adapter information') # Print an error message

MAC(x)

