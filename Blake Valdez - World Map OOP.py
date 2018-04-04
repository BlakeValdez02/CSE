class Room(object):
    def __init__(self, name, north):
        self.name = name
        self.north = north

def move(self, direction):
    global current_node
    current_node = globals()[getattr(self, direction)]


hdum = Room()
room1 = Room()
room2 = Room()

current_node = hdum
directions = ['north', 'south', 'east', 'west']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            print(hdum)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")


