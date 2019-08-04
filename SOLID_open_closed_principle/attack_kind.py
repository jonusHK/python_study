# (계속 변화하는)공격 종류를 추상화한다.
# 다형성을 이용 
# OPEN FOR EXTENSION
# 공격 종류를 확장한다.

# 시스템이 확장할 때 (EXTENSION에서)
# '변화하는 부분' --> 추상 클래스를 통해 추상화 하고!!
# 확장되는 부분을 상속을 통해 클래스를 확장한다!! 
from abc import ABCMeta, abstractmethod


# factory : 상황에 따라 
# 상황에 알맞는 객체를 반환해준다.
#  객체 생성을 위임 받았다!!
# => abstract factory design pattern
def AttackKindFactory(kind):
    if kind=='Fire':
        return FireAttackKind()
    elif kind=='Ice':
        return IceAttackKind()
    elif kind=='Stone':
        return StoneAttackKind()
    elif kind=='Kungfu':
        return KungfuAttackKind()


# abstract class
class AttackKind(metaclass=ABCMeta):
    @classmethod
    def __get_attack_kind(cls):
        return cls.__name__.replace('AttackKind', '')

    def __init__(self):
        self.kind = self.__get_attack_kind()

    def get_kind(self):
        return self.kind

    @abstractmethod
    def attack(self):
        pass

# 게임 개발 초기에 확정된 두 개의 공격 종류

class FireAttackKind(AttackKind):
    def attack(self):
        print(f"under the attack of {self.get_kind()}")

class IceAttackKind(AttackKind):
    def attack(self):
        print(f'under the attack of {self.get_kind()}')

# 추후 게임 규모가 커지면서 두 개의 공격 종류가 확장(EXTENSION)

class StoneAttackKind(AttackKind):
    def attack(self):
        print('Aimming at the player!')

class KungfuAttackKind(AttackKind):
    def attack(self):
        print('Kungfu!!')

class ArrowAttackKind(AttackKind):
    def attack(self):
        print('arrow!!')