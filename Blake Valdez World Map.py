world_map = {
    'OUTSIDE': {
        'NAME': 'Construction Site',
        'DESCRIPTION': 'You are at a construction site at a house. You can either go downstairs, east, or south.',
        'PATHS': {
            'DOWNSTAIRS': 'BASEMENT STAIRS',
            'EAST': 'GARAGE DOORS',
            'SOUTH': 'PORCH'
        }
    },
    'BASEMENT STAIRS': {
        'NAME': 'Basement outside stairs',
        'DESCRIPTION': 'You are outside the downstairs basement entrance, and you can either go east, or back upstairs.',
        'PATHS': {
            'EAST': 'DEPOT',
            'UPSTAIRS': 'OUTSIDE'
        }
    },
    'GARAGE DOORS': {
        'NAME': 'Garage doors.',
        'DESCRIPTION': 'You are in front of the garage doors. You can either go inside or back west.',
        'PATHS': {
            'INSIDE': 'GARAGE',
            'WEST': 'OUTSIDE'
        }
    },
    'PORCH': {
        'NAME': 'Front of Porch',
        'DESCRIPTION': 'You are on the front porch of the house You can either go south or back north.',
        'PATHS': {
            'SOUTH': 'LOBBY',
            'NORTH': 'OUTSIDE'
        }
    },
    'LOBBY': {
        'NAME': 'Lobby',
        'DESCRIPTION': 'You are in the lobby. You can either go upstairs, southeast, west, or back north.',
        'PATHS': {
            'UPSTAIRS': 'UPPER HALLWAY',
            'SOUTHEAST': 'KITCHEN',
            'WEST': 'LIVING ROOM',
            'NORTH': 'PORCH'
        }
    },
    'DEPOT': {
        'NAME': 'Depot',
        'DESCRIPTION': 'You are in the depot. You can either go south, or back west.',
        'PATHS': {
            'SOUTH': 'TRAINING ROOM',
            'WEST': 'OUTSIDE'
        }
    },
    'GARAGE': {
        'NAME': 'Garage',
        'DESCRIPTION': 'You are inside the garage. You can either go west, or back outside. Wow is that a lambo?!',
        'PATHS': {
            'WEST': 'LAUNDRY ROOM',
            'OUTSIDE': 'GARAGE DOORS'
        }

    },
    'LAUNDRY ROOM': {
        'NAME': 'Laundry Room',
        'DESCRIPTION': 'You are now in the laundry room. You can either go back north to the training room, or west to'
                       'the garage.',
        'PATHS': {
            'NORTH': 'DEPOT',
            'WEST': 'GARAGE'
        }
    },
    'TRAINING ROOM': {
        'NAME': 'Training Room',
        'DESCRIPTION': 'You are now in the training room. There are weights around. You seem weak, maybe lift a bit?'
                       'You can either go north to the depot, or west to the Laundry room.',
        'PATHS': {
            'WEST': 'LAUNDRY ROOM',
            'NORTH': 'DEPOT'
        }
    },

}


current_node = world_map['OUTSIDE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UPSTAIRS', 'DOWNSTAIRS', 'INSIDE', 'OUTSIDE', 'SOUTHEAST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")









