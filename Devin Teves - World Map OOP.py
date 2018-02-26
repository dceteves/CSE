class Room(object):
    def __init__(self, name, description, paths):
        self.NAME = name
        self.DESCRIPTION = description
        self.PATHS = paths

    def print_name(self):
        print(self.NAME)

    def print_description(self):
        print(self.DESCRIPTION)


BEDROOM = Room("Bedroom",
               "You are in a bedroom full of anime posters, figures, etc."
               "\nYou have a computer sitting on a desk to your north, and a door to the east.",
               {"NORTH":"COMPUTER",
                "EAST": "HALLWAY"})
HALLWAY = Room("Hallway",
               "The hallway has a few paintings with a dull red carpet on the wooden floor."
               "\nThere are stairs leading down to the south, as well as another room across yours.",
               {"WEST": "BEDROOM",
                "EAST": "BATHROOM",
                "DOWN": "DINING ROOM",
                "SOUTH": "EMPTY ROOM"})

current_node = BEDROOM
dir1 = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while True:
    current_node.print_name()
    current_node.print_description()
    command = input('>')
    if command == 'quit':
        quit(0)
    elif command.upper() in dir1:
        try:
            current_node = current_node.PATHS[command]
        except KeyError:
            print("You can't go this way.")
    else:
        print("Command not Recognized")

