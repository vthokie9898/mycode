        'Hall': {
            'south': 'Kitchen'
            },
        'Kitchen' {
            'north': 'Hall'
            }
        }

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:
    showStatus()
    
# get the player's next 'move'
# .split() breakes it up into a list array
# eg typing 'go east' would give the list:
# ['go': 'east']
move == ''
while move == '':
    move = input('>')
move = move.lower().split()

# if they type 'go ' first
if move[0] == 'go':
    # check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
        #set the current room to the new room
        currentRoom = rooms[currentRoom][move[1]
    #there is no door (link) to the new room
    else:
    print('You can\'t go that way!')
    
# if they type 'get' first
if move[0] == 'get' :
#if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

