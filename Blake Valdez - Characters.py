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
        self.name = name
        self.hp = health
        self.attack = attack
        self.dead = death
        self.dialogue = dialogue
        self.description = description
        self.status_effect = status_effect
        self.reaction = reaction
