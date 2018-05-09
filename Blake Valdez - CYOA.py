class InvalidNumberError(Exception):
    def __init__(self):
        super(InvalidNumberError, self).__init__()


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
                                                  'battle rifle, with 20 damage, and a fire rate of 4.', 20)
        self.fire_rate = 4


class M4(Gun):
    def __init__(self, name='M4'):
        super(M4, self).__init__(name, 'Medium', 'The M4 carbine is extensively used by the United States Armed Forces '
                                                 'and is largely replacing the M16 rifle in United States Army and '
                                                 'United States Marine Corps combat units as the primary '
                                                 'infantry weapon, with a 30 damage, and a fire rate of 3', 30)
        self.fire_rate = 3


class PumpShotgun(Gun):
    def __init__(self, name='Pump Shotgun'):
        super(PumpShotgun, self).__init__(name, 'Large', 'Mossberg 500 .410 Bore Special Purpose Cruiser Pump Action '
                                                         'Shotgun 18-1/2" Barrel 6 Rounds Synthetic Stock, with a '
                                                         'damage of 50 and a fire rate of 1.', 50)
        self.fire_rate = 1


class M1911(Gun):
    def __init__(self, name='M1911'):
        super(M1911, self).__init__(name, 'Small', 'The M1911 is a single-action, semi-automatic, magazine-fed, '
                                                   'recoil-operated pistol chambered for the .45 ACP cartridge. It '
                                                   'served as the standard-issue sidearm for the United States Armed '
                                                   'Forces from 1911 to 1986, with a damage of 20, and a fire '
                                                   'rate of 1.', 20)

        self.fire_rate = 1


class DP28(Gun):
    def __init__(self, name='DP28'):
        super(DP28, self).__init__(name, 'Large', 'The Degtyaryov machine gun or DP-28 is a light machine gun firing '
                                                  'the 7.62×54mmR cartridge that was primarily used by the Soviet '
                                                  'Union starting in 1928, with a damage of 50 and a fire rate '
                                                  'of 2', 50)
        self.fire_rate = 2


class Armor(Item):
    def __init__(self, name, size, description, defence):
        super(Armor, self).__init__(name, size, description)
        self.defence = defence


class FullBodyArmor(Armor):
    def __init__(self, name='FullBodyArmor'):
        super(FullBodyArmor, self).__init__(name, 'Large', 'The Full Body Armor is a three piece armor set including '
                                                           'a chestplate, leggings, and boots, providing 75 Shield. '
                                                           'In order to get the extra full 100, you need to '
                                                           'find the helmet.', 75)


class Helmet(Armor):
    def __init__(self, name='Helmet'):
        super(Helmet, self).__init__(name, 'Small', 'The Helmet is an iron helmet providing 25 extra HP. If you '
                                                    'want the extra full 100 Shield, you need to find the Full '
                                                    'Body Armor.', 25)


class Consumable(Item):
    def __init__(self, name, size, description, effect):
        super(Consumable, self).__init__(name, size, description)
        self.effect = effect


class EnergyDrink(Consumable):
    def __init__(self, name='EnergyDrink'):
        super(EnergyDrink, self).__init__(name, 'Small', 'This is the energy drink, it is a consumable, and it is '
                                                         'effects are as follows: +50 HP', 50)


class Apple(Consumable):
    def __init__(self, name='Apple'):
        super(Apple, self).__init__(name, 'Small', 'This is the apple, it is a consumable, and its effects are as '
                                                   'follows: Slow Regeneration', 25)


class MedKit(Consumable):
    def __init__(self, name='MedKit'):
        super(MedKit, self).__init__(name, 'Medium', 'This is the Med Kit. It is a consumable, and its effects are as '
                                                     'follows: Full HP.', 100)


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
        self.inventory = []
        self.shield = 0

    def attack(self, target):
        target.take_damage(self.attack_amt)

    def take_damage(self, dmg):
        damage_taken = dmg - self.shield
        if damage_taken < 0:
            damage_taken = 0
        self.hp -= damage_taken

    def move(self, direction):
        self.location = globals()[getattr(self.location, direction)]
        # ####Wiebe Note: Add Char to Room so all Chars can move

    def equip(self, item):
        if isinstance(item, Gun):
            self.attack_amt = item.damage
            print("You have equipped the %s" % item.name)
        elif isinstance(item, Armor):
            self.shield = item.defence
            print("You have equipped the %s" % item.name)

    def use(self, item):
        if isinstance(item, Consumable):
            self.hp += item.effect
            if self.hp > 100:
                self.hp = 100
            print("You use the %s" % item.name)


player = Character("You", 100, 25, False, None, None, None, None)
enemy = Character("Enemy", 100, 10, False, None, None, None, None)


class Room(object):
    def __init__(self, name, description, north, south, east, west, northeast, southeast, southwest, northwest, up,
                 down, inside, outside, item=None, enemy=0):
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
        self.enemy = enemy

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
                                                              "site. "
                                                              "There is"
                                                              " a "
                                                              "backpack"
                                                              " here. "
                                                              "You can "
                                                              "either "
                                                              "go south"
                                                              " to the "
                                                              "main "
                                                              "entrance"
                                                              ", east "
                                                              "to the "
                                                              "outside"
                                                              " garage"
                                                              " doors, "
                                                              "or down "
                                                              "to the "
                                                              "basement"
                                                              " outside"
                                                              " stairs.", None, "main_entrance", "outside_garage_doors",
                                 None, None, None, None, None, None, "basement_outside_stairs", None, None, backpack)

main_entrance = Room("Front Porch House Main Entrance", "You are at "
                                                        "the front "
                                                        "entrance of "
                                                        "a house. "
                                                        "There is an"
                                                        " energy "
                                                        "drink here."
                                                        " You can "
                                                        "wither go "
                                                        "north to "
                                                        "the "
                                                        "constructio"
                                                        "n site or "
                                                        "south to "
                                                        "the lobby.", 'outside_construction_site', 'lobby', None, None,
                     None, None, None, None, None, None, None, None, energy_drink, 0)

lobby = Room("Main Lobby", "You are in the "
                           "lobby. There is an apple here. You can "
                           "either go north "
                           "to the main "
                           "entrance, west to "
                           "the living room "
                           "southeast to the "
                           "kitchen, or up "
                           "to the lobby "
                           "stairs.", "main_entrance", None, None, "living_room", None, "kitchen", None, None,
             "lobby_stairs", None, None, None, apple, 0)

living_room = Room("Living Room", "You are in the living "
                                  "room. There is an M1911 Pistol here. Type 'stats M1911' to show stats of the M1911.",
                                  None, None, "lobby", None, None, None, None, None, None, None, None, None,
                   m1911, 1)

kitchen = Room("Kitchen", "You are in "
                          "the kitchen", None, None, "dining_room", None, None, None, None, "lobby", None, None, None,
               None, helmet, 0)

dining_room = Room("Dining Room", "You are in "
                                  "the dining "
                                  "room", None, None, None, "kitchen", None, None, None, None, None, None, None,
                   None, med_kit, 0)

lobby_stairs = Room("Lobby Stairs", "You are upstairs", None, "upper_hallway", None, None, None, None, None, None, None,
                    "Lobby", None, None, None, 2)

upper_hallway = Room("Upstairs Hallway", "You are in the upper "
                                         "hallway", "workshop", "kids_bedroom", "bathroom", None, None,
                     "master_bedroom", None, None, None, None, None, None, pump_shotgun, 0)

workshop = Room("Workshop", "You are in "
                            "the workshop", None, "upper_hallway", None, None, None, None, None, None, None, None, None,
                None, None, 0)

kids_bedroom = Room("Kids Bedroom", "You are in the "
                                    "kids bedroom", "upper_hallway", None, None, None, None, None, None, None, None,
                    None, None, None, full_body_armour, 3)

bathroom = Room("Bathroom", "You are in "
                            "the bathroom", None, "master_bedroom", None, "upperhallway", None, None, None, None, None,
                None, None, None, None, 0)

master_bedroom = Room("Master Bedroom", "You are in "
                                        "the master "
                                        "bedroom", "bathroom", None, None, None, None, None, None, "upper_hallway",
                      None, None, None, None, None, 0)

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


def fight(modifier):
    current_enemy = Character("Enemy", 100 + modifier, 10, False, None, None, None, None)
    print("You have %d health" % player.hp)
    print("The enemy has %d health" % current_enemy.hp)
    print()
    print("A Wild Enemy appears!!!")
    while current_enemy.hp > 0 and player.hp > 0:
        options = ["Attack", "Nothing", "Drink energy Drink"]
        for num, action in enumerate(options):
            print(str(num + 1) + ": " + action)
        try:
            cmd = int(input("What do you want to do?"))
            if cmd < 1 or cmd > len(options):
                raise InvalidNumberError
            if cmd == 1:
                player.attack(current_enemy)
                print("The enemy has %d health left" % current_enemy.hp)
        except ValueError:
            print("That is not a number")
            continue
        except InvalidNumberError:
            print("Invalid Number")
            continue

        current_enemy.attack(player)
        print("You have %d health left" % player.hp)
        if player.hp <= 0:
            print("YOU LOSE!!!!!")
            quit(0)


current_node = outside_construction_site
directions = ['north', 'south', 'east', 'west', 'up', 'down', 'northeast', 'northwest', 'southeast', 'southwest',
              'inside', 'outside']
short_directions = ['n', 's', 'e', 'w', 'u', 'd', 'ne', 'nw', 'se', 'sw', 'in', 'out']
health_modifier = 0


while True:
    print(current_node.name)
    print(current_node.description)
    while current_node.enemy > 0:
        fight(health_modifier)
        health_modifier += 25
        current_node.enemy -= 1
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
    elif command == 'stats M1911':
        print('The M1911 is a single-action, semi-automatic, magazine-fed, '
              'recoil-operated pistol chambered for the .45 ACP cartridge. It '
              'served as the standard-issue sidearm for the United States Armed '
              'Forces from 1911 to 1986, with a damage of 20, and a fire '
              'rate of 1.')

    elif command == 'stats DP28':
        print('The Degtyaryov machine gun or DP-28 is a light machine gun firing '
              'the 7.62×54mmR cartridge that was primarily used by the Soviet '
              'Union starting in 1928, with a damage of 50 and a fire rate '
              'of 2',)

    elif command == 'stats pumpshotgun':
        print('Mossberg 500 .410 Bore Special Purpose Cruiser Pump Action '
              'Shotgun 18-1/2" Barrel 6 Rounds Synthetic Stock, with a '
              'damage of 50 and a fire rate of 1.')

    elif command == 'stats G36':
        print('Classic assault rifle, designed in the early 1990s by Heckler & Koch'
              ' in Germany as a replacement for the heavier 7.62mm G3 '
              'battle rifle, with 20 damage, and a fire rate of 4.')

    elif command == 'stats M4':
        print('The M4 carbine is extensively used by the United States Armed Forces '
              'and is largely replacing the M16 rifle in United States Army and '
              'United States Marine Corps combat units as the primary '
              'infantry weapon, with a 30 damage, and a fire rate of 3')

    elif current_node.item is not None and 'take' in command:
        player.inventory.append(current_node.item)
        current_node.item = None
        print("Taken.")
    elif 'equip ' in command:
        item_requested = command[6:]
        found = False
        for item in player.inventory:
            if item.name.lower() == item_requested.lower():
                found = True
                player.equip(item)
        if not found:
            print("You don't have that")
    elif 'use ' in command:
        item_requested = command[4]
        found = False
        for item in player.inventory:
            if item.name.lower() == item_requested.lower():
                found = True
                player.use(item)
    else:
        print("Command not recognized")
