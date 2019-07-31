#!/usr/bin/env python3

loginfail = 0
login = 0
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")
#keystone_file_lines=keystone_file.readlines()
for i in keystone_file:
    if "- - - - -] Authorization failed" in i:
        loginfail += 1 # this is the same as loginfail = loginfail + 1
for i in keystone_file:
    if "-] Authorization failed" in i:
        login += 1 
print("The number of failed log in attempts is " + str(loginfail))
print("The number of successful log in attempts is " + str(login))

