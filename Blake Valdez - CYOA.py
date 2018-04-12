class Item(object):
    def __init__(self, name, size, description):
        self.name = name
        self.size = size
        self.description = description

    def look(self):
        print(self.description)


class Gun(Item):
    def __init__(self, name, size, description, damage_stat):
        super(Gun, self).__init__(name, size, description)
        self.damage = damage_stat

    def shoot(self, target):
        target.take_damage(self.damage)  # Take_damage is a method in the character class


class G36(Gun):
    def __init__(self, name='G36'):
        super(G36, self).__init__(name, 'medium', 'Classic assault rifle, designed in the early 1990s by Heckler & Koch'
                                                  ' in Germany as a replacement for the heavier 7.62mm G3 '
                                                  'battle rifle.', 20)
        self.fire_rate = 4


class M4(Gun):
    def __init__(self, name='M4'):
        super(M4, self).__init__(name, 'Medium', 'The M4 carbine is extensively used by the United States Armed Forces '
                                                 'and is largely replacing the M16 rifle in United States Army and '
                                                 'United States Marine Corps combat units as the primary '
                                                 'infantry weapon', 30)
        self.fire_rate = 3


class PumpShotgun(Gun):
    def __init__(self, name='Pump Shotgun'):
        super(PumpShotgun, self).__init__(name, 'Large', 'Mossberg 500 .410 Bore Special Purpose Cruiser Pump Action '
                                                         'Shotgun 18-1/2" Barrel 6 Rounds Synthetic Stock', 50)
        self.fire_rate = 1


class M1911(Gun):
    def __init__(self, name='M1911'):
        super(M1911, self).__init__(name, 'Small', 'The M1911 is a single-action, semi-automatic, magazine-fed, '
                                                   'recoil-operated pistol chambered for the .45 ACP cartridge. It '
                                                   'served as the standard-issue sidearm for the United States Armed '
                                                   'Forces from 1911 to 1986', 20)

        self.fire_rate = 1


class Armor(Item):
    def __init__(self, name, size, description, damage_stat):
        super(Armor, self).__init__(name, size, description)
        self.damage = damage_stat

    def shoot(self, target):
        target.take_damage(self.damage)


class Character(object):
    def __init__(self, name, health, attack, death, dialogue, description, status_effect, reaction, location=None):
        self.name = name  # String
        self.hp = health  # int
        self.attack_amt = attack  # int
        self.dead = death   # boolean
        self.dialogue = dialogue  #
        self.description = description
        self.status_effect = status_effect
        self.reaction = reaction
        self.location = location

    def attack(self, target):
        target.take_damage(self.attack_amt)

    def take_damage(self, dmg):
        self.hp -= dmg

    def move(self, direction):
        self.location = globals()[getattr(self.location, direction)]
        # ####Wiebe Note: Add Char to Room so all Chars can move


player = Character("You", 100, 25, False, None, None, None, None)
enemy = Character("Enemy", 100, 10, False, None, None, None, None)

player.attack(enemy)
print(enemy.hp)


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


outside_construction_site = Room("Outside Construction Site", "Description", None, "main_entrance", "garage_doors",
                                 None, None, None, None, None, None, "basement_outside_stairs")
main_entrance = Room("Front Porch House Main Entrance", "Description", 'outside_construction_site', 'lobby', None, None,
                     None, None, None, None, None, None)
lobby = Room("Main Lobby", "Description", "main_entrance", None, "")

player.location = outside_construction_site
directions = ['north', 'south', 'east', 'west', 'up', 'down', 'northeast', 'northwest', 'southeast', 'southwest']
short_directions = ['n', 's', 'e', 'w', 'u', 'd', 'ne', 'nw', 'se', 'sw']


while True:
    print(player.location.name)
    print(player.location.description)
    command = input('>_')
    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command == 'quit':
        quit(0)
    elif command in directions:
        try:
            player.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")





