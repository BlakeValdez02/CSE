# Create a Character Class. It must have at least 5 instance variables. All five instance MUST be used. It must also
# have at least 2 methods
# NAME
# HEALTH
# PICK UP ITEMS
# MOVE?
# ATTACK
# DEATH
# DIALOGUE
# PERFORM ACTION (use, push, etc)
# DESCRIPTION
# STATUS EFFECT (PARALYZE, POISON, BURN, ETC)
# TAKE DAMAGE


class Character(object):
    def __init__(self, name, health, attack, death, dialogue, description, status_effect, reaction):
        self.name = name  # String
        self.hp = health  # int
        self.attack_amt = attack  # int
        self.dead = death   # boolean
        self.dialogue = dialogue  #
        self.description = description
        self.status_effect = status_effect
        self.reaction = reaction

    def attack(self, enemy):
        enemy.take_damage(self.attack_amt)

    def take_damage(self, dmg):
        self.hp -= dmg


player = Character("You", 100, 25, False, None, None, None, None)
enemy = Character("Enemy", 100, 10, False, None, None, None, None)

player.attack(enemy)
print(enemy.hp)