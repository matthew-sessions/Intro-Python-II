from room import Room
from player import Player
import time
from move_logic import *
from item import Item

# Declare all the rooms

def dots(n):
    for i in range(n):
        time.sleep(.17)
        print('*')


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('knife', '🔪')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('sword', '⚔️'), Item('hammer', '🔨')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 
[Item('gun', '🔫'), Item('rope', '📿')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('matthew', room['outside'])

print(f'Hello {player.name}! Welcome to the game!')

dots(5)


move = input("Type press anything to start or press q to quit!")
dots(2)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while move != 'q':
    dots(5)
    print(f"Location: {player.current_room.name}")
    dots(2)
    print(f"{player.current_room.description}")
    dots(2)
    proom_items(player.current_room)
    dots(1)
    puser_items(player)
    move = move_check()
   
    if move in ['n', 'e', 's', 'w']:
        try:
            player.current_room = getattr(player.current_room, f'{move}_to')
        except:
            print('You hit a wall, try again')
    else:
        if move.lower().split(' ')[0] == 'get':
            try:
                res = get_item(player.current_room, move)
                player.item.append(res)
                player.current_room.item.remove(res)
                print(player.item[-1].on_take)
            except:
                print('Item not in room')

        else:
            try:      
                res = get_item(player, move)
                player.current_room.item.append(res)
                player.item.remove(res)
                print(player.current_room.item[-1].on_take)
            except:
                print('You do not have this item.')