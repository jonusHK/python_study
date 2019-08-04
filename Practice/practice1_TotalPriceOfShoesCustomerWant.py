from collections import Counter

shoes_num = int(input())  # 6

shoes_size = input()  # 5 6 7 8 8 5
shoes_size = shoes_size.split(" ")  # shoes_size = ['5', '6', '7', '8', '8', '5']
counter_shoes = Counter(shoes_size) # Counter({'5': 2, '6': 1, '7': 1, '8': 2})
counter_shoes_var = dict(counter_shoes)

customer_num = int(input())   # 6

want_count = 0
price = 0
while want_count < customer_num:
    want_list = input()  # 6 55
    want_list = want_list.split(" ")   # want_list = ['6', '55']

    if counter_shoes_var.get(want_list[0]) != None and counter_shoes_var[want_list[0]] != 0:
        price += int(want_list[1])
        counter_shoes_var[want_list[0]] -= 1

    want_count += 1

print(price)
