class Account:
    num_of_account = 0
    interest_rate = 0.08
    @staticmethod
    def func(a, b):
        return a + b

    @classmethod
    def string_constructor(cls, string):
        clnt_name = string.split('_')[0]
        __balance = int(string.split('_')[1])
        return cls(clnt_name, __balance)

    @classmethod
    def get_num_of_account(cls):
        return cls.num_of_account

    def __init__(self, clnt_name, balance):
        self.clnt_name = clnt_name
        self.__balance = balance
        Account.num_of_account += 1

    def deposit(self, money):
        if money < 0:
            print('입금액은 0보다 커야 합니다.')
            return
        self.__balance += money

    def withdraw(self, money):
        if money < 0:
            print('출금액은 0보다 커야 합니다.')
            return False
        elif self.__balance < money:
            print(f'출금액은 {self.__balance}원을 초과할 수 없습니다.')
            return
        self.__balance -= money

    def __str__(self):
        return f'{self.clnt_name}님의 현재 잔고는 {self.__balance}원입니다.'

if __name__ == "__main__":
    customer1 = Account.string_constructor('hyeounkeun_10000')
    customer2 = Account('moonkeun', 20000)
    customer3 = Account('haeryong', 30000)
    print(Account.get_num_of_account())
    
    customer1.deposit(20000)
    print(customer1)
    customer1.withdraw(5000)
    print(customer1)
    print(customer1.withdraw(-50))

    # customer2.deposit(10000)
    # print(customer2)
    # customer2.withdraw(10000)
    # print(customer2)

    # print(Account.func(10000, 20000))


    