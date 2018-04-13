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


outside_construction_site = Room("Outside Construction Site", "You are outside "
                                                              "at a "
                                                              "construction "
                                                              "site", None, "main_entrance", "outside_garage_doors",
                                 None, None, None, None, None, None, "basement_outside_stairs", None, None)
main_entrance = Room("Front Porch House Main Entrance", "You are at "
                                                        "the front "
                                                        "entrance of "
                                                        "a house", 'outside_construction_site', 'lobby', None, None,
                     None, None, None, None, None, None, None, None)
lobby = Room("Main Lobby", "You are in the "
                           "lobby", "main_entrance", None, None, "living_room", None, "kitchen", None, None,
             "lobby_stairs", None, None, None)
living_room = Room("Living Room", "You are in the living "
                                  "room", None, None, "lobby", None, None, None, None, None, None, None, None, None)
kitchen = Room("Kitchen", "You are in "
                          "the kitchen", None, None, "dining_room", None, None, None, None, "lobby", None, None, None,
               None,)
dining_room = Room("Dining Room", "You are in "
                                  "the dining "
                                  "room", None, None, None, "kitchen", None, None, None, None, None, None, None,
                   None,)
lobby_stairs = Room("Lobby Stairs", "You are upstairs", None, "upper_hallway", None, None, None, None, None, None, None,
                    "Lobby", None, None)
upper_hallway = Room("Upstairs Hallway", "You are in the upper "
                                         "hallway", "workshop", "kids_bedroom", "bathroom", None, None,
                     "master_bedroom", None, None, None, None, None, None)
workshop = Room("Workshop", "You are in "
                            "the workshop", None, "upper_hallway", None, None, None, None, None, None, None, None, None,
                None)
kids_bedroom = Room("Kids Bedroom", "You are in the "
                                    "kids bedroom", "upper_hallway", None, None, None, None, None, None, None, None,
                    None, None, None)
bathroom = Room("Bathroom", "You are in "
                            "the bathroom", None, "master_bedroom", None, "upperhallway", None, None, None, None, None,
                None, None, None)
master_bedroom = Room("Master Bedroom", "You are in "
                                        "the master "
                                        "bedroom", "bathroom", None, None, None, None, None, None, "upper_hallway",
                      None, None, None, None)
outside_garage_doors = Room("Garage Doors (outside)", "You are outside "
                                                      "in front of an "
                                                      "open garage", None, None, None, "outside_construction_site",
                            None, None, None, None, None, None, "garage", None)
garage = Room("Garage", "You are in the "
                        "garage", None, None, None, "laundry_room", None, None, None, None, None, None, None,
              "outside_garage_doors")
laundry_room = ("Laundry Room", "You are in the"
                                "laundry room", "training_room", None, "garage", None, None, None, None, None, None,
                None, None, None)

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
