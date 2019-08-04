# 확장할 때 마다 Character 클래스와
# Monster 클래스의 코드가 변한다.

from abc import ABCMeta, abstractmethod
# from attack_before import Attacks
from attack_kind import AttackKindFactory

# abstract class
# parent class
class Character(metaclass=ABCMeta):
    # class member <-- composition
    # 전역변수를 대체할 수 있다.
    attacks=Attacks()

    def __init__(self, name, hp, power):
        self.name=name
        self.hp=hp
        self.power=power

    # 추상 메서드
    # 바디(body)가 없는 함수
    # 반드시 하나 이상 존재해야
    # 추상 클래스로 만들 수 있다.
    @abstractmethod
    def attack(self, other, kind):
        pass

    @abstractmethod
    def get_damage(self, power, attack_kind):
        pass

    def __str__(self):
        return f'{self.name} : {self.hp}'

# Character 클래스를 상속하므로, attack, get_damage를 반드시 재정의(메서드 오버라이딩)
# 다형성을 강제
class Player(Character):
    def __init__(self, name='player', hp=100, power=10, *attack_kinds):
        # 부모 클래스의 생성자 --> name, hp, power
        # 위임
        super().__init__(name, hp, power)

        # 새롭게 추가된 멤버
        self.skills=[]
        for attack_kind in attack_kinds:     # attack_kinds = FireAttakKind(), ...
            self.skills.append(attack_kind)

    def attack(self, other, a_kind):
        for attack_kind in self.skills:
            if attack_kind.get_kind() == a_kind:
                other.get_damage(self.power, a_kind)
                # 다형성 코드
                attack_kind.attack()

    def get_damage(self, power, a_kind):
        for attack_kind in self.skills:
            if a_kind == attack_kind.get_kind():
                self.hp -= (power // 2)
                return

        self.hp -= power

class Monster(Character):
    @classmethod
    def get_monster_kind(cls):
        return cls.__name__.replace('Monster', '')

    def __init__(self, name='Monster', hp=50, power=5):
        super().__init__(name, hp, power)
        self.name = self.get_monster_kind() + name
        # 핵심 코드!!
        # AttackKindFactory를 통해서 얻을 수 있는 것들을 이해하는 것이 핵심이다!
        self.attack_kind = AttackKindFactory(self.get_monster_kind())

    def attack(self, other, a_kind):
        if a_kind == self.attack_kind.get_kind():
            other.get_damage(self.power, a_kind)
            return
        self.attack_kind.attack()
            
    def get_damage(self, power, a_kind):
        if a_kind == self.attack_kind.get_kind():
            self.hp += power
        else:
            self.hp -= power

    def get_attack_kind(self):
        return self.attack_kind.get_kind()

    @abstractmethod
    def generate_gold(self):
        pass
