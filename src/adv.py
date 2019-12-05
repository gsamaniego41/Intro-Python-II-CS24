from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Items

flashlight = Item('Flashlight', 'Lights up the path.')
sword = Item('Sword', 'Liquid Sword from the Wu.')
shield = Item('Shield', 'Shield made of vibranium.')
zune = Item('Zune', 'To listen to phat beats while adventuring.')

# Add items

room['outside'].add_item(flashlight)
room['foyer'].add_item(sword)
room['narrow'].add_item(shield)
room['treasure'].add_item(zune)

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

# initial commit

commands = ('n', 's', 'e', 'w', 'q')
options = ('y', 'n')

# Decorations
dashes = '------------------'
stars = '***************'
exclamation1 = '!!!!!!!!!!!!!!!!!!!'
exclamation2 = '¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡'


def endgame():
    print('\n>>>>> You quit the game. <<<<<\n')
    quit()


def play_game(name):
    global player
    explore = ''

    if player.current_room == None:
        print(
            f"\n{exclamation1}\nDead End. No room there...\nStarting over. -_-\n{exclamation2}\n")
        player.current_room = room['outside']

    else:
        print(
            f'\nCurrent Room:\n{dashes}\nYou are at the {player.current_room}\n')
        map = f'Directions:\n{dashes}\nNorth: {player.current_room.n_to}\n{dashes}\nSouth: {player.current_room.s_to}\n{dashes}\nEast: {player.current_room.e_to}\n{dashes}\nWest: {player.current_room.w_to}\n{dashes}\n'
        print(map)

        # Explore the room

        while explore not in options:
            explore = input("Explore the room (y/n)? ")
            if explore == 'q':
                endgame()
            elif explore not in options:
                print(f'\nPls select a valid command\n{options}\n')
            elif explore == "y":
                if len(player.current_room.items) > 0:
                    print(
                        f"\nYou found this item: \n{player.current_room.items[0].name} - {player.current_room.items[0].desc}\n")
                    pickup_item = input(
                        "Pick it up (y/n)? ")
                    if pickup_item == 'q':
                        endgame()
                    elif pickup_item not in options:
                        print(f'\nPls select a valid command\n{options}\n')
                    elif pickup_item == 'y':
                        player.add_item(player.current_room.items[0])
                        player.current_room.remove_item(
                            player.current_room.items[0])

                else:
                    print(
                        f"\n{exclamation1}\nNo items were found\n{exclamation2}\n")
            else:
                pass

        # Move player
        location = input("Where would you like to go next? ")

        if location not in commands:
            print(f'\nPls select a valid command\n{commands}\n')

        elif location == "n":
            player.current_room = player.current_room.n_to

        elif location == "s":
            player.current_room = player.current_room.s_to

        elif location == "e":
            player.current_room = player.current_room.e_to

        elif location == "w":
            player.current_room = player.current_room.w_to

        elif location == "q":
            endgame()


name = input('What\'s your name? ')
player = Player(name)
player.current_room = room['outside']
print(f'\n{stars}\nWelcome {name}!\n{stars}\n')


while True:
    play_game(name)
