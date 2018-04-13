class Room(object):
    def __init__(self, name, description, north, south, east, west, northeast, southeast, southwest, northwest, up,
                 down, inside, outside):
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
        self.inside = inside
        self.outside = outside

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

# Need 15 Rooms.


outside_construction_site = Room("Outside Construction Site", "Description", None, "main_entrance", "garage_doors",
                                 None, None, None, None, None, None, "basement_outside_stairs", None, None)
main_entrance = Room("Front Porch House Main Entrance", "Description", 'outside_construction_site', 'lobby', None, None,
                     None, None, None, None, None, None, None, None)
lobby = Room("Main Lobby", "Description", "main_entrance", None, None, "living_room", None, "kitchen", None, None,
             "lobby_stairs", None, None, None)
living = Room("Living Room", "Description", None, None, "lobby", None, None, None, None, None, None, None, None, None)
kitchen = Room("Kitchen", "Description", None, None, "dining_room", None, None, None, None, "Lobby", None, None, None,
               None,)
dining_room = Room("Dining Room", "Description", None, None, None, "kitchen", None, None, None, None, None, None, None
                   None)
lobby_stairs = Room("Lobby Stairs", "Description", None, "upper_hallway", None, None, None, None, None, None, None,
                    "Lobby", None, None)
upper_hallway = Room("Upstairs Hallway", "Description", "workshop", "kids_bedroom", "bathroom", None, None,
                     "master_bedroom", None, None, None, None, None, None)
workshop = Room("Workshop", "Description", None, "upper_hallway", None, None, None, None, None, None, None, None)
kids_bedroom = Room("Kids Bedroom", "description", "upper_hallway", None, None, None, None, None, None, None, None,
                    None)
bathroom = Room("Bathroom", "Description", None, "master_bedroom", None, "upperhallway", None, None, None, None, None,
                None)
master_bedroom = Room("Master Bedroom", "Description", "bathroom", None, None, None, None, None, None, "upper_hallway",
                      None, None)
outside_garage_doors = Room("Garage Doors (outside)", "Description", None, None, None, "outside_construction_site",)

current_node = outside_construction_site
directions = ['north', 'south', 'east', 'west', 'up', 'down', 'northeast', 'northwest', 'southeast', 'southwest',
              'inside', 'outside']
short_directions = ['n', 's', 'e', 'w', 'u', 'd', 'ne', 'nw', 'se', 'sw', 'in', 'out']


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


