world_map = {
    'OUTSIDE': {
        'NAME': 'Construction Site',
        'DESCRIPTION': 'You are at a construction site. There is a house to the south.',
        'PATHS': {
            'WEST': 'BASEMENT',
            'EAST': 'GARAGE',
            'SOUTH': 'PORCH'
        }
    },
    'PORCH': {
        'NAME': 'Front of Porch',
        'DESCRIPTION': 'You are on the front of the house.',
        'PATHS': {
            'SOUTH': 'LOBBY',
            'NORTH': 'OUTSIDE'
        }
    },
    'BASEMENT': {
        'NAME': 'Basement outside stairs',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'EAST': 'DEPOT'
        }
    },
    'LOBBY': {
        'NAME': '',
        'DESCRIPTION': '',
        'PATHS': {

        }
    }
}

current_node = world_map['OUTSIDE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UPSTAIRS', 'DOWNSTAIRS']

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









        