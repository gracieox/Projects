#gracie oxnam
#adventure game day 1


rooms = {"room1":{"S": "room2", "E": "room4"},
         "room2":{"E": "room3", "N": "room1"},
         "room3":{"N": "room4", "W": "room2"},
         "room4":{"E": "room5", "S": "room3", "W": "room1"},
         "room5":{"S": "room6", "W": "room4"},
         "room6":{"N": "room5"}}

def choose_direction(room):
    print("you are in a room. there are doors in the following directions")
    print(rooms[room.keys("")])
    #asks user to choose a direction
    direction = input("Which direction would you like to travel? ")
        #if user inputs invalid, tell them no, and ask again
        #if direction == rooms.
        #return the new room (based on direction chosen)
    return room[direction]
        
choose_direction("room1")
