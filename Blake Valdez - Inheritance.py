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
                                                  'battle rifle.', 10)
        self.fire_rate = 2


class M4(Gun):
    def __init__(self, name='M4'):
        super(M4, self).__init__(name, 'Large', '' 20)
        self.fire_rate = 2




