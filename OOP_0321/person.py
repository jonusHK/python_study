class Person:
    def __init__(self, name, balance):
        self.name = name
        # if balance < 0:
        #     try:
        #         self.__balance = self.__balance
        #     except AttributeError:
        #         self.__balance = 0
        #     finally:
        #         return

        self.__balance = balance

        self.age = None # 인스턴스멤버를 안쓰더라도 __init__에 None으로 선언해주는게 좋음

    # getter
    @property
    def balance(self):
        print('getter executed')
        return self.__balance

    @balance.setter
    def balance(self, money):
        print('setter executed')
        if money < 0:
            try:
                self.__balance = self.__balance
            except AttributeError:
                self.__balance = 0
            finally:
                return

        self.__balance = money


    # access function
    # getter
    # def get_money(self):
    #     return self.__balance

    # access function
    # setter
    # def set_money(self, money):
    #     self.__balance = money


if __name__ == "__main__":
    # 객체의 멤버에 접근(getter)이나 수정(setter)을 할 때는
    # 메서드(access function)를 이용한다.
    # print(john.get_money())
    # john.set_money(4000)

    # USER 프로그래머는 객체의 멤버처럼 취급하면 된다.
    # 하지만 내부적으로는 getter 혹은 setter를 호출한다.
    # 반드시 메서드를 통해 실제 멤버에 접근
    # getter
    # john = Person('john', 0)
    # john.balance = -5000
    # print(john.balance)
    # john.balance = 5000
    # print(john.balance)
    # john.balance = -5000
    # print(john.balance)

    john = Person('john', -5000)
    print(john.balance)
    john = Person('john', 5000)
    print(john.balance)
    john = Person('john', -5000)
    print(john.balance)

    # setter
    # john.balance = 6000