# module/characters.py

class Character:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

class Hero(Character):
    def __init__(self, name, hp, mp, skill):
        super().__init__(name, hp, mp)
        self.skill = skill

    def use_skill(self):
        if self.mp >= self.skill.mp_cost:
            self.mp -= self.skill.mp_cost
            return True
        return False
    
class Skill:
    def __init__(self, name, mp_cost):
        self.name = name
        self.mp_cost = mp_cost


class Dragon(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp, 0)
