class Room(object):
    def __init__(self, name, description, north, south, east, west, northeast, southeast, southwest, northwest, up,
                 down):
        self.name = name
        self.north = north
        self.description = description
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.southwest = southwest
        self.northwest = northwest
        self.northeast = northeast
        self.up = up
        self.down = down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

# Need 15 Rooms.


outside_construction_site = Room("Outside Construction Site", "Description", None, "main_entrance", "garage_doors",
                                 None, None, None, None, None, None, "basement_outside_stairs")
main_entrance = Room("Front Porch House Main Entrance", "Description", 'outside_construction_site', 'lobby', None, None,
                     None, None, None, None, None, None)
lobby = Room("Main Lobby", "Description", "main_entrance", None, None, "living_room", None, "kitchen", None, None,
             "lobby_stairs", None)
living = Room("Living Room", "Description", None, None, "lobby", None, None, None, None, None, None, None)
kitchen = Room("Kitchen", "Description", None, None, None, None, None, None, None, "Lobby", None, None)
lobby_stairs = Room("Lobby Stairs", "Description", None, "upper_hallway", None, None, None, None, None, None, None,
                    "Lobby")
upper_hallway = Room("Upstairs Hallway", "Description", "workshop", "kids_bedroom", "bathroom", None, )



current_node = outside_construction_site
directions = ['north', 'south', 'east', 'west', 'up', 'down', 'northeast', 'northwest', 'southeast', 'southwest']
short_directions = ['n', 's', 'e', 'w', 'u', 'd', 'ne', 'nw', 'se', 'sw']


while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_')
    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command == 'quit':
        quit(0)
    elif command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")


