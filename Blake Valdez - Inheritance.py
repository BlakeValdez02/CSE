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
                                                           'purchase the helmet.', 75)


class Helmet(Armor):
    def __init__(self, name='Helmet'):
        super(Helmet, self).__init__(name, 'Small', 'The Helmet is an iron helmet providing 25 extra HP. If you '
                                                    'want the extra full 100 HP, you need to purchase the Full '
                                                    'Body Armor.', 25)


class Consumable(Item):
    def __init__(self, name, description, effect):
        super(Consumable, self).__init__(name, description)
        self.effect = effect

        