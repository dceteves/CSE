import time
import random

# colored text
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

counter = 0
inventory = []
invCapacity = 8
health = 100
onFire = False


class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down, character, item):
        self.NAME = name
        self.DESCRIPTION = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.up = up
        self.down = down
        self.character = character
        self.item = item
        self.looping_oof = ["oof"]
        self.ping_phrases = ['pls', 'pls stop', 'pls stop doing this', 'pls just continue the game',
                             'just play the game', 'y u do dis', 'stop', 'stop doing this']

    def print_descriptions(self):
        print(BLUE + self.NAME + END)
        print(self.DESCRIPTION)
        if current_node.item is not None and current_node.item.isTaken is False and current_node_hasChanged:
            print("It seems you can take a... " + current_node.item.name.lower())

    def move(self, directions):
        global current_node
        current_node = globals()[getattr(self, directions)]

    def jump(self):
        if current_node == BEDROOM or current_node == LIVING_ROOM:
            time.sleep(.5)
            print(BOLD + "oh woop there's a ceiling fan there" + END)
            time.sleep(1)
            print(RED + "You hit the ceiling fan while it was on. Your head gets chopped off" + END)
            quit(0)
        else:
            print(RED + BOLD + "ow" + END)
            time.sleep(.5)

    def oof(self):
        print(BOLD + "".join(self.looping_oof) + END)
        time.sleep(.5)
        self.looping_oof.append("oof")

    def ping(self):
        if counter <= 2:
            print(BOLD + UNDERLINE + "pong" + END)
        elif counter == 3:
            print(GREEN + BOLD + "don't waste your time doing this" + END)
        elif counter == 4:
            print(YELLOW + BOLD + "pls you have more important things other than this" + END)
        elif counter == 5:
            print(CYAN + BOLD + "pls" + END)
        elif counter <= 9:
            print(BOLD + PURPLE + random.choice(self.ping_phrases) + END)
        elif counter == 10:
            print(RED + BOLD + "You typed in ping too much that the game got tired of you and decided to quit")
            quit(0)

    def flush(self):
        if current_node == BATHROOM:
            print(BOLD + "..." + END)
            time.sleep(1)
            print(BOLD + RED + "a man rises from the toilet and kills you" + END)
            quit(0)
        else:
            print(RED + BOLD + "There's no toilet here u stupid" + END)


class Character(object):
    def __init__(self, name, description, dialogue, inv, hp):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.inventory = inv
        self.health = hp
        self.isAlive = True
        self.hasTalked = False
        self.counter = 0  # counter for number of encounters of character

    def print_descriptions(self):
        print(GREEN + BOLD + self.name + END)
        print(self.description)

    def talk(self):
        print("He says...")
        time.sleep(1)
        print(self.dialogue)
        time.sleep(.5)
        self.hasTalked = True

    def kill(self):
        print(BOLD + RED + "oh woops you killed " + self.name.lower() + END)
        self.isAlive = False
        # if None not in self.inventory:


class Item(object):
    def __init__(self, name):
        self.name = name
        self.isTaken = False

    def take(self):
        if len(inventory) == invCapacity:
            print(RED + BOLD + "Your inventory is full." + END)
        else:
            inventory.append(self)
            print(CYAN + BOLD + "You take the " + self.name.lower() + "." + END)
            self.isTaken = True

    def drop(self):
        inventory.pop(inventory.index(self))
        print(CYAN + BOLD + "You drop the " + self.name.lower() + END)
        current_node.item = self
        self.isTaken = False


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage

    def hit(self): current_node.character.health -= self.damage

    def check_stats(self): print(BOLD + BLUE + "Damage: " + END + str(self.damage))


class Sword(Weapon):
    def __init__(self, name, damage):
        super(Sword, self).__init__(name, damage)


class Hammer(Weapon):
    def __init__(self, name):
        super(Hammer, self).__init__(name, 1)

    def break_door(self):
        print(BOLD + "..." + END)
        time.sleep(1)
        print(BOLD + BLUE + "Why is this hammer made of rubber?" + END)


class Food(Item):
    def __init__(self, name, effect):
        super(Food, self).__init__(name)
        self.effect = effect
        self.isEaten = False
        self.counter = 0

    def eat(self):
        self.isEaten = True
        inventory.pop(self.index())


class Container(Item):
    def __init__(self, name, capacity):
        super(Container, self).__init__(name)
        self.capacity = capacity
        self.inventory = []

    def put_item_in(self, item):
        if self.inventory.len() == capacity:
            print(RED + BOLD + "Your inventory is full." + END)
        else:
            self.inventory.append(item)
            print(CYAN + BOLD + "You put the " + item.name.lower() + " in the " + self.name.lower() + '.' + END)


class Bag(Container):
    def __init__(self, name):
        super(Bag, self).__init__(name, 6)


class Jar(Container):
    def __init__(self, name):
        super(Jar, self).__init__(name, 2)


class Key(Item):
    def __init__(self, name):
        super(Key, self).__init__(name)


class Ball(Item):
    def __init__(self, name):
        super(Ball, self).__init__(name)

    def throw(self):
        if current_node == BACKYARD1 or current_node == BACKYARD2:
            if ball in inventory:
                inventory.pop(inventory.index(ball))
                print("You throw the ball and in a blink of an eye, one of the dogs zoom in a blink of an eye and catch "
                    "the ball.")
                time.sleep(4)
                print(YELLOW + BOLD + "The dog then hovers and starts floating to orbit.")
                time.sleep(3)
                print(YELLOW + BOLD + "The dog comes back with a bucket with even more balls.")
                time.sleep(1)
            else:
                print(RED + BOLD + "You don't have any tennis balls ya spud" + END)



Cookie = Character("Cookiezi", "This person seems to be sitting behind a desk with a computer, mashing his keyboard "
                               "slightly, but you could definitely hear it. On his monitor, he seems to be clicking "
                               "circles...", None, None, None)
jeff = Character("jeff", "he's sitting on a chair playing a game on the left side of the room", "stop", ['pen'], 50)

cookie = Food("Cookie", None)
bed = Item("Bed")
ball = Ball("Ball")

BEDROOM = Room("Bedroom",
               "You are in a bedroom full of anime posters, figures, etc."
               "\nYou have a computer sitting on a desk to your north, and a door to the east.",
               "COMPUTER", None, "HALLWAY", None, None, None, None, bed)
COMPUTER = Room("Computer",
                "On the desk lies a computer with a crappy membrane keyboard and a mouse. "
                "On the computer lies a weird game called 'osu!'...",
                None, "BEDROOM", "HALLWAY", None, None, None, None, None)
HALLWAY = Room("Hallway",
               "The hallway has a few paintings with a dull red carpet on the wooden floor."
               "\nThere are stairs leading down to the south, as well as another room across yours.",
               "DINING_ROOM", "EMPTY_ROOM", "BATHROOM", "BEDROOM", None, "DINING_ROOM", None, None)
EMPTY_ROOM = Room("Empty Room",
                  "You enter an empty room, but in the southern-most corner there's a table with what seems to be "
                  "a drawing tablet, as well as a keyboard.",
                  "HALLWAY", "TABLE", None, None, None, None, jeff, None)
TABLE = Room("Table", "On the table there are empty boxes with labels saying 'HyperX Alloy FPS Mechanical Gaming "
                      "Keyboard' as well as another box that says 'Huion Graphics Tablet'...",
             "EMPTY_ROOM", None, None, None, None, None, None, None)
BATHROOM = Room("Bathroom",
                "The bathroom is set with two sinks, a bathtub and a toilet. "
                "There are also toiletries sitting on top of the sink counter.",
                None, None, None, "HALLWAY", None, None, None, None)
DINING_ROOM = Room("Dining Room",
                   "The dining room has a table with a fancy green cloth and a basket full of fake fruit."
                   "\nThe kitchen leads east, and the living room to the west.",
                   None, "HALLWAY", "KITCHEN1", "LIVING_ROOM", "HALLWAY", None, None, cookie)
KITCHEN1 = Room("Entrance to Kitchen",
                "In the kitchen there's a refrigerator and a pantry full of "
                "food, as well as a long counter to eat food on.\nThere's more stuff farther south.",
                "DINING_ROOM", "KITCHEN2", None, None, None, None, None, None)
KITCHEN2 = Room("Farther Side of Kitchen",
                "This side of the Kitchen has a flat screen tv mounted to the wall with a smaller table below "
                "it that holds the cable box, and an old, useless game console.\nThere's what seems to be a "
                "laundry room to the west as well as a slide door leading outside east.",
                "KITCHEN1", None, "BACKYARD1", "LAUNDRY_ROOM", None, None, None, None)
LAUNDRY_ROOM = Room("Laundry Room",
                    "The Laundry Room has a washing and drying machine, as well as a cabinet.",
                    "CABINET", None, "KITCHEN2", None, None, None, None, None)
CABINET = Room("Inside of Cabinet",
               "Inside the cabinet contains jackets and sweaters. The shelf above it has a few boxes put for "
               "storage, but there's a paper mask of a man's face with glasses smiling and squinting his "
               "eyes...",  # osu! joke, don't worry about it
               None, "LAUNDRY_ROOM", "KITCHEN2", None, None, None, None, None)
BACKYARD1 = Room("Backyard",
                 "The empty backyard had little to no grass, making it look like a desert. Not only that, there "
                 "are two dogs that seem to not care about it at all and just have fun with the tennis balls "
                 "around them.", "BACKYARD2", None, None, "KITCHEN2", None, None, None, ball)
BACKYARD2 = Room("Farther side of the Backyard",
                 "This side of the backyard has an unused grill and a bench lying at the wall of the house. And "
                 "more tennis balls...", None, "BACKYARD1", None, None, None, None, None, ball)
LIVING_ROOM = Room("Living Room",
                   "The living room has couches set with a large TV.\nThe exit seems to go the south.",
                   None, "DOOR", "DINING_ROOM", None, None, None, None, None)
DOOR = Room("Door",
            "You stand at the exit of the house, where lies a bunch of shoes.\nThe door faces west, "
            "and there's another door to the south.",
            "LIVING_ROOM", "LOCKED_DOOR", None, 'PORCH', None, None, None, None)
LOCKED_DOOR = Room("Locked Door", "This room's door is locked.", "DOOR", None, None, None, None, None, None, None)
PORCH = Room("Porch",
             "You exit the house into the porch, where there are short, dull, plants.\nYou can go more to "
             "the west to exit the porch and into the driveway.",
             None, None, "DOOR", "DRIVEWAY", None, None, None, None)
DRIVEWAY = Room("Driveway",
                "The drive way has a basketball hoop, but to the west you see a store with a sign that says... "
                "Walm.\nYou can go back north into the porch.", "PORCH", None, None, "STORE", None, None, None, None)
STORE = Room("Walm", "Sorry to keep your hopes up, this store is closed.",
             None, None, "DRIVEWAY", None, None, None, None, None)

"""
LOCKED_DOOR = Room("Tech Room",
                   "The door you break leads you into room filled with bright looking technology. The whole "
                   "room seems to be white-ish. The whole room seems to be some sort of 'man cave'. You feel "
                   "so intimidated that you shouldn't touch any of the equipment."
                   "DOOR", None, None, None, None, None, cookie)
"""

dir1 = ['north', 'south', 'east', 'west', 'up', 'down']
dir2 = ['n', 's', 'e', 'w', 'u', 'd']

current_node = BEDROOM
current_node_hasChanged = True

while True:
    print(RED + BOLD + "Health: " + END + str(health))
    if current_node_hasChanged:
        current_node.print_descriptions()
        current_node_hasChanged = False
    if current_node.character is not None and current_node.character.isAlive and \
            current_node.character.hasTalked is False:
        current_node.character.print_descriptions()
    command = input('>').lower().strip()
    if command == 'quit':
        quit(0)
    elif health == 0:
        break
    elif command == 'look' or command == 'l':
        current_node.print_descriptions()
        if current_node.character is None:
            continue
        else:
            current_node.character.print_descriptions()
    elif command == "jump":
        current_node.jump()
    elif command == 'inv' or command == 'inventory':
        if not inventory:
            print(RED + BOLD + "You don't have anything in your inventory." + END)
        else:
            print("Your inventory:")
            for item in inventory:
                print(BOLD + item.name.lower() + END)
    elif command == "oof":
        current_node.oof()
    elif command == "ping":
        current_node.ping()
        counter += 1
    elif command == 'flush':
        current_node.flush()
    elif command in dir2:
        pos = dir2.index(command)
        command = dir1[pos]
        try:
            current_node.move(command)
            current_node_hasChanged = True
        except KeyError:
            print(RED + "You can't go that way." + END)
            current_node_hasChanged = False
    elif command in dir1:
        try:
            current_node.move(command.lower())
            current_node_hasChanged = True
        except KeyError:
            print(RED + "You can't go that way." + END)
            current_node_hasChanged = False
    elif 'take' in command:
        if current_node.item.name.lower() in command:
            if current_node.item.isTaken is False:
                if current_node.item == bed:
                    print(BOLD + "..." + END)
                    time.sleep(1)
                    print(BOLD + "Well, if that's what you want.")
                    time.sleep(1)
                    current_node.item.take()
                else:
                    current_node.item.take()
            else:
                print(RED + BOLD + "You already took that." + END)
        else:
            take_command = input("What do you want to take?\n>").lower().strip()
            if take_command == current_node.item.name.lower():
                if current_node.item.isTaken is False:
                    if current_node.item == bed:
                        print(BOLD + "..." + END)
                        time.sleep(1)
                        print(BOLD + "Well, if that's what you want.")
                        time.sleep(1)
                        current_node.item.take()
                    else:
                        current_node.item.take()
                else:
                    print(RED + BOLD + "You already took that." + END)
            else:
                print(RED + BOLD + "That isn't here." + END)
    elif 'drop' in command:
        splitCmd = command.split()
        if not inventory:
            print(RED + BOLD + "You don't have anything in your inventory." + END)
        for item1 in inventory:
            if item1.name.lower() in command:
                item1.drop()
            else:
                print(RED + BOLD + "That's not in your inventory." + END)
                break
    elif 'throw' in command:
        if 'ball' in command:
            ball.throw()
        else:
            throw_command = input("What do you want to throw?\n>").lower()
            if throw_command == 'ball':
                ball.throw()
            else:
                for item in inventory:
                    if throw_command == item:
                        item.drop()
                        break
                    else:
                        print(RED + BOLD + "That's not in your inventory." + END)

    else:
        print("Command not Recognized")
        current_node_hasChanged = False
