class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down):
        self.NAME = name
        self.DESCRIPTION = description
        self.NORTH = north
        self.SOUTH = south
        self.WEST = west
        self.EAST = east
        self.UP = up
        self.DOWN = down

    def print_name(self):
        print(self.NAME)

    def print_description(self):
        print(self.DESCRIPTION)


BEDROOM = Room("Bedroom",
               "You are in a bedroom full of anime posters, figures, etc."
               "\nYou have a computer sitting on a desk to your north, and a door to the east.",
               True, False, True, False, False, False)
COMPUTER = Room("Computer",
                "On the desk lies a computer with a crappy membrane keyboard and a mouse. "
                "On the computer lies a weird game called 'osu!'...",
                False, True, True, False, False, False)
HALLWAY = Room("Hallway",
               "The hallway has a few paintings with a dull red carpet on the wooden floor."
               "\nThere are stairs leading down to the south, as well as another room across yours.",
               False, True, True, True, True, False)
EMPTY_Room = Room("Empty Room",
                  "You enter an empty room, but in the southern-most corner there's a table with what seems to be "
                  "a drawing tablet, as well as a keyboard.",
                  True, True, False, False, False, False)
TABLE = Room("Table",
             "On the table there's a long box with a label saying 'HyperX Alloy FPS Mechanical Gaming "
             "Keyboard' as well as another box that says 'Huion Graphics Tablet'...",
             True, False, False, False, False, False)
BATHROOM = Room("Bathroom",
                "The bathroom is set with two sinks, a bathtub and a toilet. "
                "There are also toiletries sitting on top of the sink counter.",
                False, False, False, True, False, False)
DINING_ROOM = Room("Dining Room",
                   "The dining room has a table with a fancy green cloth and a basket full of fake fruit."
                   "\nThe kitchen leads east, and the living room to the west.",
                   False, False, True, True, True, False)
KITCHEN1 = Room("Entrance to Kitchen",
                "In the kitchen there's a refrigerator and a pantry full of "
                "food, as well as a long counter to eat food on.\nThere's more stuff farther south.",
                True, True, False, False, False, False)
KITCHEN2 = Room("Farther Side of Kitchen",
                "This side of the Kitchen has a flat screen tv mounted to the wall with a smaller table below "
                "it that holds the cable box, and an old, useless game console.\nThere's what seems to be a "
                "laundry room to the west as well as a slide door leading outside east.",
                True, True, True, True, False, False)
LAUNDRY_ROOM = Room("Laundry Room",
                    "The Laundry Room has a washing and drying machine, as well as a cabinet.",
                    True, False, True, False, False, False)
CABINET = Room("Inside of Cabinet",
               "Inside the cabinet contains jackets and sweaters. The shelf above it has a few boxes put for "
               "storage, but there's a paper mask of a man's face with glasses smiling and squinting his "
               "eyes...",  # osu! joke, don't worry about it
               False, True, True, False, False, False)
BACKYARD1 = Room("Backyard",
                 "The empty backyard had little to no grass, making it look like a desert. Not only that, there "
                 "are two dogs that seem to not care about it at all and just have fun with the tennis balls "
                 "around them.",
                 True, False, False, True, False, False)
BACKYARD2 = Room("Farther side of the Backyard",
                 "This side of the backyard has an unused grill and a bench lying at the wall of the house. And "
                 "more tennis balls...",
                 False, True, False, False, False, False)
LIVING_ROOM = Room("Living Room",
                   "The living room has couches set with a large TV.\nThe exit seems to go the south.",
                   False, True, True, False, False, False)
DOOR = Room("Door",
            "You stand at the exit of the house, where lies a bunch of shoes.\nThe door faces west, "
            "and there's another door to the south.",
            True, True, False, True, False, False)
LOCKED_DOOR = Room("Locked Door",
                   "This room's door is locked.",
                   True, False, False, False, False, False)
PORCH = Room("Porch",
             "You exit the house into the porch, where there are short, dull, plants.\nYou can go more to "
             "the west to exit the porch and into the driveway.",
             False, False, True, True, False, False)
DRIVEWAY = Room("Driveway",
                "The drive way has a basketball hoop, but to the south you see a store with a sign that says... "
                "Walm.\nYou can go back north into the porch.",
                True, False, False, True, False, False)
STORE = Room("Walm",
             "Sorry to keep your hopes up, this store is closed.",
             False, False, True, False, False, False)

current_node = BEDROOM
# dir1 = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while True:
    current_node.print_name()
    current_node.print_description()
    command = input('>')
    if command == 'quit':
        quit(0)

    else:
        print("Command not Recognized")

