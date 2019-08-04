class Account:
    # 클래스 멤버(class member)
    # 모든 객체가 공유한다.
    # 전역변수(global variable)를 대체한다.
    # 이자율
    interest_rate = 0.08
    num_of_account = 0

    # 클래스 메서드(class method)
    # 객체가 하나도 없는 상태에서도 호출이 가능!!
    # 전역 함수(global variable)를 대체
    # 전역 변수를 대체할 때는 static method를 쓸 수도 있다.
    # 대체 생성자(alternative constructor) 

    # staticmethod : 메서드처럼 보이지만 함수(전역 함수이지만 그나마 관련있는 클래스에 속하고 한 것)
    @staticmethod
    def func(a, b):
        return a + b    

    @classmethod
    def get_num_of_account(cls):
        """
        Account.get_num_of_account() -> integer
        return : 개설된 계좌 수
        """
        return cls.num_of_account

    # 대체 생성자
    @classmethod
    def string_constructor(cls, string):   # string = 'john_10000'
        data = string.split('_')   # 'data = ['john', '10000']
        clnt_name = data[0]    # clnt_name = 'john'
        balance = int(data[1])  # balance = 10000
        return cls(clnt_name, balance)   # return -> 'john', 10000
 
    # 생성자(constructor) : 파이썬에서는 오직 하나!
    # 객체(object)가 생성될 때 반드시 한번 호출된다.
    def __init__(self, clint_name, balance):
        # 인스턴스 멤버(instance member)
        self.clnt_name = clint_name
        # __인스턴스변수 : 이건 비공개야! 외부에서 쓰지마!
        self.__balance = balance    # _Account__balance

        #클래스 멤버에 접근하는 방법 1
        #클래스 멤버에 접근하는 방법 2
        Account.num_of_account += 1  # self.num_of_account += 1 사용 불가
    # 인스턴스 메서드(instance method)

    def deposit(self, money): 
        '''
        a.deposit(money) -> boolean
        만약에 money > 0 이면 입금 성공!
        아니면 에러 메시지 출력 후 실패!
        '''
        if money < 0 :
            print("입금은 0원 초과부터 가능합니다.")
            return False
        self.__balance += money
        return True

    # 인스턴스 메서드
    def withdraw(self, money):
        '''
        a.withdraw(money) -> integer
        return : 인출된 돈
        만약 잔고가 모자라면 None
        '''
        if self.__balance < money:
            print(f"출금은 {self.__balance} 미만으로 가능합니다.")
            return None
        else:
            self.__balance -= money
            return money

    def transfer(self, other, money):
        # 내 객체가 가진 돈
        self.__balance -= money
        
        # message passing
        # 다른 객체의 상태 정보(인스턴스 멤버)를 변경할 때는
        # 반드시 상대 객체가 가진 메서드를 이용
        other.deposit(money)

    def __str__(self):
        return f"{self.clnt_name} : {self.__balance}"

if __name__ == "__main__":
    # customer = Account.string_constructor('hyeonkeun_10000')
    # print(customer.clnt_name, customer._Account__balance)
    # # 객체 생성
    # my_acnt = Account('greg', 5000)
    # your_acnt = Account('john', 2000)

    # # instance method 호출하는 방법
    # my_acnt.deposit(7000)
    # print(my_acnt)

    # # 메서드 : 입력 + 인스턴스 멤버(상태정보, 데이터)에 의해 결과 값이 결정
    #         # 인스턴스 멤버(상태 정보)를 바꾸는 역할!
    # # 함수 : 입력에 의해서 출력이 결정
    # res1 = my_acnt.withdraw(3000)
    # res2 = your_acnt.withdraw(3000)

    # print(my_acnt)
    # print(your_acnt)

    # # 객체 간에 상호 작용 --> 객체가 갖고 있는 멤버의 값(데이터, 상태 정보)이 달라짐
    # # INTERACTION by 메서드
    # my_acnt.transfer(your_acnt, 1000)

    # 대체 생성자를 이용한 객체의 생성
    # s = 'james_6000'
    # his_acnt = Account.string_constructor(s)
    # print(his_acnt)

    customer_1 = Account('john', 10000)
    customer_2 = Account('josh', 20000)

    Account.string_constructor('john_10000')

    a = Account('josh', 10000)
    