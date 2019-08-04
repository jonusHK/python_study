from abc import ABCMeta, abstractmethod

class Characters(metaclass = ABCMeta):
    def __init__(self, name, HP, power):
        self.name = name
        self.HP = HP
        self.power = power

    @abstractmethod
    def attack(self, other, attack_kind):
        pass
    @abstractmethod
    def get_damage(self, power, attack_kind):
        pass
    
    def __str__(self):
        return f'{self.name} : {self.HP}'

class Player(Characters):
    def __init__(self, name = 'player', HP = 100, power = 10, *attack_kinds):
        super().__init__(name, HP, power)

        self.skills = []
        for attack_kind in attack_kinds:   # attack_kinds = [FireAttackKind, IceAttackKind, ...]
            self.skills.append(attack_kind)

    def attack(self, other, a_kind):   # a_kind = [Fire, Ice, ...]
        for attack_kind in self.skills:
            if attack_kind.get_kind() == a_kind:
                other.get_damage(self.power, a_kind)

    def get_damage(self, power, a_kind):
        for attack_kind in self.skills:
            if attack_kind.get_kind == a_kind:
                self.HP -= power // 2
            else:
                self.HP -= power

class Monster(Characters):
    @classmethod
    def get_monster_kind(cls):
        return cls.__name__.replace('Monster','')

    def __init__(self, name = 'Monster', HP = 50, power = 5):
        super().__init__(name, HP, power)
        self.name = self.get_monster_kind + name
        self.attack_kind = AttackKindFactory(self.get_monster_kind)

    def attack(self, other, attack_kind):
        if self.attack_kind
