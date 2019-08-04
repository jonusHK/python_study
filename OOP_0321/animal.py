# abc : abstract base class (추상 베이스 클래스)
from abc import ABCMeta, abstractmethod

# Animal 객체를 생성할 수 없도록 만든 코드 ↓↓↓
class Animal(metaclass = ABCMeta):
    @abstractmethod
    def say(self):
        pass

class Lion(Animal):    # Lion클래스도 추상클래스가 된다.
    pass

class Duck(Animal):
    def say(self):
        print('꽥꽥')

class Dog(Animal):
    def say(self):
        print('멍멍')

class Deer(Animal):
    def say(self):
        print('사슴')


if __name__ == "__main__":
    animals = []
    animals.extend((Lion(), Duck(), Deer(), Dog(), Duck()))  # --> Lion는 추상클래스이므로, 객체 생성이 불가능하다.

    # ani = Animal()   # --> 오류발생
    # ani.say()

    for animal in animals:
        animal.say()