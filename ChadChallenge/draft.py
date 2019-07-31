#!/usr/bin/env python3
# Author: Trotta

message = "You are on the clock!"
print("How many touchdowns did your potential pick have in 2018? ")
touchdowns = float(input())

if touchdowns == 0:
    message = message + ' This better be a rookie or someone that was hurt last year that you are betting your season on'
elif touchdowns <= 4:
    message = message + ' WTF are you doing?  You want the first pick in next year\'s draft don\'t you?'
elif touchdowns <= 8:
    message = message + ' Really?  Only 1 touchdown every other game?  DO NOT DRAFT'
elif touchdowns <= 12:
    message = message + ' Hopefully this isn\'t the first round of the draft.  Draft with caution'
elif touchdowns <= 16:
    message = message + ' Not bad for a backup, if drafting as a starter keep looking'
elif touchdowns <= 20:
    message = message + ' Could be a starter if no other options are available.'
else:
    message = message + ' Draft immediately'
print(message)
print("Script has completed")

