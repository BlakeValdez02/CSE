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


class DP28(Gun):
    def __init__(self, name='DP28'):
        super(DP28, self).__init__(name, 'Large', 'The Degtyaryov machine gun or DP-28 is a light machine gun firing '
                                                  'the 7.62×54mmR cartridge that was primarily used by the Soviet '
                                                  'Union starting in 1928.', 50)
        self.fire_rate = 2


class Armor(Item):
    def __init__(self, name, size, description, defence):
        super(Armor, self).__init__(name, size, description)
        self.defence = defence


class FullBodyArmor(Armor):
    def __init__(self, name='FullBodyArmor'):
        super(FullBodyArmor, self).__init__(name, 'Large', 'The Full Body Armor is a three piece armor set including '
                                                           'a chestplate, leggings, and boots, providing 75 more '
                                                           'HP. In order to get the extra full 100, you need to '
                                                           'find the helmet.', 75)


class Helmet(Armor):
    def __init__(self, name='Helmet'):
        super(Helmet, self).__init__(name, 'Small', 'The Helmet is an iron helmet providing 25 extra HP. If you '
                                                    'want the extra full 100 HP, you need to find the Full '
                                                    'Body Armor.', 25)


class Consumable(Item):
    def __init__(self, name, size, description, effect):
        super(Consumable, self).__init__(name, size, description)
        self.effect = effect


class EnergyDrink(Consumable):
    def __init__(self, name='EnergyDrink'):
        super(EnergyDrink, self).__init__(name, 'Small', 'This is the energy drink, it is a consumable, and it is '
                                                         'effects are as follows: Speed Boost, Slow Healing.', 'Speed'
                                                                                                               'Boost,'
                                                                                                               ' Slow '
                                                                                                               'Regener'
                                                                                                               'ation.')


class Apple(Consumable):
    def __init__(self, name='Apple'):
        super(Apple, self).__init__(name, 'Small', 'This is the apple, it is a consumable, and its effects are as '
                                                   'follows: Slow Regeneration', 'Slow Regeneration.')


class MedKit(Consumable):
    def __init__(self, name='MedKit'):
        super(MedKit, self).__init__(name, 'Medium', 'This is the Med Kit. It is a consumable, and its effects are as '
                                                     'follows: Full HP.', 'Full Health')


class Backpack(Item):
    def __init__(self, name='BackPack'):
        super(Backpack, self).__init__(name, 'Large', 'This is the Backpack, It is your extra space.')


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
                 down, inside, outside, item=None, enemy=None):
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
        self.item = item
        self.enemy = enemy(+1)

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


g36 = G36()
m4 = M4()
pump_shotgun = PumpShotgun()
m1911 = M1911()
dp28 = DP28()
full_body_armour = FullBodyArmor()
helmet = Helmet()
energy_drink = EnergyDrink()
apple = Apple()
med_kit = MedKit()
backpack = Backpack()

outside_construction_site = Room("Outside Construction Site", "You are outside "
                                                              "at a "
                                                              "construction "
                                                              "site", None, "main_entrance", "outside_garage_doors",
                                 None, None, None, None, None, None, "basement_outside_stairs", None, None, backpack)
main_entrance = Room("Front Porch House Main Entrance", "You are at "
                                                        "the front "
                                                        "entrance of "
                                                        "a house", 'outside_construction_site', 'lobby', None, None,
                     None, None, None, None, None, None, None, None, energy_drink)
lobby = Room("Main Lobby", "You are in the "
                           "lobby", "main_entrance", None, None, "living_room", None, "kitchen", None, None,
             "lobby_stairs", None, None, None, apple)
living_room = Room("Living Room", "You are in the living "
                                  "room", None, None, "lobby", None, None, None, None, None, None, None, None, None,
                   m1911)
kitchen = Room("Kitchen", "You are in "
                          "the kitchen", None, None, "dining_room", None, None, None, None, "lobby", None, None, None,
               None, helmet)
dining_room = Room("Dining Room", "You are in "
                                  "the dining "
                                  "room", None, None, None, "kitchen", None, None, None, None, None, None, None,
                   None, )
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
