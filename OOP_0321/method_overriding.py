class CarOwner:
    def __init__(self, name):
        self.name = name

    def concentrate(self):
        print(f'{self.name} is concentrating!')

class Car:
    def __init__(self, owner_name):
        self.car_owner = CarOwner(owner_name)

    def drive(self):
        self.car_owner.concentrate()
        print(f'{self.car_owner.name} is driving!')

class SelfDrivingcar(Car):
    # 비슷한 기능을 자식에 맞춰서
    # 메서드를 재정의하는 것(메서드 오버라이딩)
    def drive(self):
        print("driving by itself")

if __name__ == "__main__":
    car1 = Car('john')
    car2 = Car('james')
    car3 = SelfDrivingCar('yang')

    car = []
    cars.extend((car1, car2, car3))

    # 다형성 코드
    # 객체에 따라 코드가 다양해지게 된다.(drive함수를 revoke 하는 객체가 다르므로)
    for car in cars:
        car.drive()