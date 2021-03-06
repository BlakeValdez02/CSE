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
        self.can_pick_up = False

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

    def take(self, item):
        if isinstance(item, Backpack):
            self.can_pick_up = True
        if self.can_pick_up:
            self.inventory.append(item)
            return True
        else:
            print("You have nowhere to put it.")
            return False

    def use(self, item):
        if isinstance(item, Consumable):
            self.hp += item.effect
            if self.hp > 100:
                self.hp = 100
            print("You use the %s" % item.name)

    def drink_energy_drink(self):
        item_to_remove = None
        for item in self.inventory:
            if isinstance(item, EnergyDrink):
                self.hp += 50
                print("You drink the energy drink")
                item_to_remove = item
                break
        if item_to_remove is not None:
            self.inventory.remove(item_to_remove)
        else:
            print("You don't have an energy drink.")

    def eat_apple(self):
        item_to_remove = None
        for item in self.inventory:
            if isinstance(item, Apple):
                self.hp += 25
                print("You eat the apple")
                item_to_remove = item
                break
        if item_to_remove is not None:
            self.inventory.remove(item_to_remove)
        else:
            print("You don't have an apple.")

    def use_med_kit(self):
        item_to_remove = None
        for item in self.inventory:
            if isinstance(item, MedKit):
                self.hp += 100
                print("You use the MedKit.")
                item_to_remove = item
                break
        if item_to_remove is not None:
            self.inventory.remove(item_to_remove)
        else:
            print("You don't have an medkit.")

    def use_helmet(self):
        item_to_remove = None
        for item in self.inventory:
            if isinstance(item, Helmet):
                self.hp += 25
                print("You use the helmet. You now have 25 extra HP.")
                break
        if item_to_remove is not None:
            self.inventory.remove(item_to_remove)
        else:
            print("You don't have an medkit.")


player = Character("You", 100, 25, False, None, None, None, None)
enemy = Character("Enemy", 100, 10, False, None, None, None, None)


class Room(object):
    def __init__(self, name, description, north, south, east, west, northeast, southeast, southwest, northwest, up,
                 down, inside, outside, item=None, enemy=0, item_description=""):
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
        self.item_description = item_description

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

outside_construction_site = Room("Outside Construction Site", "You are outside at a construction site. "
                                 "You can either go south to the main entrance, east to the outside garage doors, or "
                                 "down to the basement outside stairs.", None, "main_entrance", "outside_garage_doors",
                                 None, None, None, None, None, None, "basement_outside_stairs", None, None, backpack, 0,
                                 "There is a backpack here. ")

basement_outside_stairs = Room("Basement Stairs", "You are outside the basement. go Up to go to the Outside "
                                                  "Construction site, or west to the depot.", None, None, None, "depot",
                               None, None, None, None, "outside_construction_site", None, None, None, None, 2)

depot = Room("Depot", "You are in the depot. You can go east to the basement, or south to the training room.", None,
             "training_room", "basement_outside_stairs", None, None, None, None, None, None, None, None, None, None)

training_room = Room("Training Room", "You are in the Training Room, You can either go south to the Laundry Room, or "
                                      "north to the depot.", "depot", "laundry_room", None, None, None, None, None,
                     None, None, None, None, None, None, 1)

main_entrance = Room("Front Porch House Main Entrance", "You are at "
                                                        "the front "
                                                        "entrance of "
                                                        "a house. "
                                                        " You can "
                                                        "either go "
                                                        "north to "
                                                        "the "
                                                        "constructio"
                                                        "n site or "
                                                        "south to "
                                                        "the lobby.", 'outside_construction_site', "lobby", None, None,
                     None, None, None, None, None, None, None, None, energy_drink, 0, "There is an energy drink here. ")

lobby = Room("Main Lobby", "You are in the "
                           "lobby. You can "
                           "either go north "
                           "to the main "
                           "entrance, west to "
                           "the living room "
                           "southeast to the "
                           "kitchen, or up "
                           "to the lobby "
                           "stairs.", "main_entrance", None, None, "living_room", None, "kitchen", None, None,
             "lobby_stairs", None, None, None, apple, 0, "There is an apple here.")

living_room = Room("Living Room", "You are in the living "
                                  "room. You can only go east to the lobby.",
                                  None, None, "lobby", None, None, None, None, None, None, None, None, None,
                   m1911, 0, "There is an M1911 Pistol here. Type 'stats M1911' to show stats of the M1911. ")

kitchen = Room("Kitchen", "You are in "
                          "the kitchen. "
                          "You can "
                          "either go "
                          "east to the "
                          "dining room, "
                          "or northwest "
                          "to the lobby.", None, None, "dining_room", None, None, None, None, "lobby", None, None, None,
               None, helmet, 1, "There is a helmet here. ")

dining_room = Room("Dining Room", "You are in "
                                  "the dining "
                                  "room. You "
                                  "can only go "
                                  "west to the "
                                  "kitchen.", None, None, None, "kitchen", None, None, None, None, None, None, None,
                   None, med_kit, 0, "There is a Med Kit here. ")

lobby_stairs = Room("Lobby Stairs", "You are upstairs"
                                    ". You can either"
                                    " go south to the "
                                    "hallway, or down"
                                    " to the lobby.", None, "upper_hallway", None, None, None, None, None, None, None,
                    "Lobby", None, None, None, 2)

upper_hallway = Room("Upstairs Hallway", "You are in the upper "
                                         "hallway. You can either "
                                         "go north to the workshop"
                                         ", south to the kids "
                                         "bedroom east to the "
                                         "bathroom, or southeast "
                                         "to the master bedroom.", "workshop", "kids_bedroom", "bathroom", None, None,
                     "master_bedroom", None, None, None, None, None, None, pump_shotgun, 0, "There is a pump shotgun "
                                                                                            "here. Type 'stats pump "
                                                                                            "shotgun' to show the stats"
                                                                                            " of the pump shotgun.")

workshop = Room("Workshop", "You are in "
                            "the workshop"
                            ". You can "
                            "only go "
                            "south to the"
                            " hallway.", None, "upper_hallway", None, None, None, None, None, None, None, None, None,
                None, None, 2)

kids_bedroom = Room("Kids Bedroom", "You are in the "
                                    "kids bedroom. "
                                    "You can only go "
                                    "north to the "
                                    "hallway.", "upper_hallway", None, None, None, None, None, None, None, None,
                    None, None, None, full_body_armour, 0, "There is Full Body Armour here. ")

bathroom = Room("Bathroom", "You are in "
                            "the bathroom."
                            " You can "
                            "either go "
                            "south to the "
                            "master "
                            "bedroom, or "
                            "west to the "
                            "hallway.", None, "master_bedroom", None, "upperhallway", None, None, None, None, None,
                None, None, None, None, 3)

master_bedroom = Room("Master Bedroom", "You are in "
                                        "the master "
                                        "bedroom. You"
                                        " can either "
                                        "go north, or"
                                        " northwest "
                                        "to the "
                                        "hallway.", "bathroom", None, None, None, None, None, None, "upper_hallway",
                      None, None, None, None, DP28, 0, "There is a DP-28 Light Machine Gun here. Type 'stats DP28' to "
                                                       "show the stats of the DP28 Light Machine Gun.")

outside_garage_doors = Room("Garage Doors (outside)", "You are outside "
                                                      "in front of an "
                                                      "open garage. "
                                                      "You can either "
                                                      "go west to the "
                                                      "construction "
                                                      "site, or inside "
                                                      "to the garage.", None, None, None, "outside_construction_site",
                            None, None, None, None, None, None, "garage", None, M4, 0, "There is an M4 Assault Rifle "
                                                                                       "here. Type 'stats M4' to "
                                                                                       "show stats of the M4 Assault "
                                                                                       "Rifle. ")

garage = Room("Garage", "You are in the "
                        "garage. You can "
                        "either go west to"
                        " the laundry room"
                        ", or outside to "
                        "the Garage Doors "
                        "(outside).", None, None, None, "laundry_room", None, None, None, None, None, None, None,
              "outside_garage_doors", g36, 0, "There is a G36 Assault Rifle here. Type 'stats G36' to show the stats "
                                              "of the G36 Assault Rifle.")

laundry_room = Room("Laundry Room", "You are in the"
                                    " laundry room"
                                    ". You can go"
                                    " north to "
                                    "the training"
                                    " room or "
                                    "back east to"
                                    " the garage.", "training_room", None, "garage", None, None, None, None, None, None,
                    None, None, None, None, 1, )


def fight(modifier):
    current_enemy = Character("Enemy", 100 + modifier, 10, False, None, None, None, None)
    print("You have %d health" % player.hp)
    print("The enemy has %d health" % current_enemy.hp)
    print()
    print("A Wild Enemy appears!!!")
    while current_enemy.hp > 0 and player.hp > 0:
        options = ["Attack", "Nothing", "Drink energy Drink", "Eat Apple", "Use MedKit"]
        for num, action in enumerate(options):
            print(str(num + 1) + ": " + action)
        try:
            cmd = int(input("What do you want to do?"))
            if cmd < 1 or cmd > len(options):
                raise InvalidNumberError
            if cmd == 1:
                player.attack(current_enemy)
                print("The enemy has %d health left" % current_enemy.hp)
                
            elif cmd == 3:
                player.drink_energy_drink()
                print("You have %d health" % player.hp)

            elif cmd == 4:
                player.eat_apple()
                print("You have %d health" % player.hp)

            elif cmd == 5:
                player.use_med_kit()
                print("You have %d health ")

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
    print(current_node.item_description)
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
        print()
        print('The M1911 is a single-action, semi-automatic, magazine-fed, '
              'recoil-operated pistol chambered for the .45 ACP cartridge. It '
              'served as the standard-issue sidearm for the United States Armed '
              'Forces from 1911 to 1986, with a damage of 20, and a fire '
              'rate of 1.')
        print()

    elif command == 'stats DP28':
        print()
        print('The Degtyaryov machine gun or DP-28 is a light machine gun firing '
              'the 7.62×54mmR cartridge that was primarily used by the Soviet '
              'Union starting in 1928, with a damage of 50 and a fire rate '
              'of 2',)
        print()

    elif command == 'stats pumpshotgun':
        print()
        print('Mossberg 500 .410 Bore Special Purpose Cruiser Pump Action '
              'Shotgun 18-1/2" Barrel 6 Rounds Synthetic Stock, with a '
              'damage of 50 and a fire rate of 1.')
        print()

    elif command == 'stats G36':
        print()
        print('Classic assault rifle, designed in the early 1990s by Heckler & Koch'
              ' in Germany as a replacement for the heavier 7.62mm G3 '
              'battle rifle, with 20 damage, and a fire rate of 4.')
        print()

    elif command == 'stats M4':
        print()
        print('The M4 carbine is extensively used by the United States Armed Forces '
              'and is largely replacing the M16 rifle in United States Army and '
              'United States Marine Corps combat units as the primary '
              'infantry weapon, with a 30 damage, and a fire rate of 3')
        print()

    elif command == 'kill self':
        print("Suicide is not the answer. Seriously 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 "
              "1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 1-800-273-8255 ")

    elif 'take' in command:
        if current_node.item is not None and player.take(current_node.item):
            current_node.item = None
            print("Taken.")
            current_node.item_description = ""
            print()
        else:
            print()
            pass
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
        item_requested = command[4:]
        found = False
        for item in player.inventory:
            if item.name.lower() == item_requested.lower():
                found = True
                player.use(item)
    elif command in ['i', 'inventory']:
        print("You have the following items:")
        for item in player.inventory:
            print(item.name)
        print()
    else:
        print("Command not recognized")

