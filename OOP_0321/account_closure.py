def make_account(clint_name, balance):
    def money(amount):
        nonlocal balance
        balance += amount
        return (clint_name, balance)
    return money

if __name__ == "__main__":
    my_acnt = make_account('greg', 5000)
    your_acnt = make_account('john', 3000)
    result1 = my_acnt(-3000)
    result2 = your_acnt(-3000)
    print(result1 , result2)