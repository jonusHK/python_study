def fibonacci(num):
    global password
    if num == 1:
        return 1
    if num == 2:
        return password
    return fibonacci(num - 1) + fibonacci(num - 2)

# ASCII CODE --> A ~ Z : 65 ~ 90
# HELLO, WORLD! --> IFNOT, EBMTG!
def convert_to_string(str):  # str = HELLO, WORLD!    
    str_list = []
    not_str_list = {}
    for i in range(len(str)):
        if ord(str[i]) >= 65 and ord(str[i]) <= 90:   # 65 <= str[i] <= 90
            str_list.append(ord(str[i]))
            # str_list = ord[H, E, L, L, O, W, O, R, L, D]
        else:
            not_str_list[i] = str[i] # {5 : ',', 6 : ' ', 12 : '!' }

    for i in range(len(str_list)):
        str_list[i] = chr((str_list[i] + fibonacci(i + 1) - 64) % 26 + 64)
            # str_list = [I, F, N, O, T, E, B, M, T, G]
    for k, v in not_str_list.items():
        str_list.insert(k, v)
    print("".join(str_list))

password = int(input("암호키를 입력하세요: "))
convert_to_string(input("암호화할 문자열을 입력하세요: "))

'''
# SIMPLE WAY
password = int(input("암호키를 입력하세요: "))
string = input("암호화할 문자열을 입력하세요: ")
def convert(password, string):
    fibo_num = 1
    result = ''
    for str in string:
        if str.isupper():
            result += chr((ord(str) + fibo_num - 64) % 26 + 64)   # A ~ Z : 65 ~ 90
            fibo_num, password = password, fibo_num + password
        else:
            result += str
        
    print(result)

convert(password, string)
'''