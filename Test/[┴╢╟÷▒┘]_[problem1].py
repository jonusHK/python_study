# n번째 피보나치 수를 반환하는 함수를
# 재귀 함수와
# 반복문을 활용한 함수로 
# 만드세요.
# 사용자가 매개변수로 반드시 1 이상의 수를 전달한다고 가정합니다.
# (에러 핸들링 하지 않으셔도 됩니다.)

# 0 1 1 2 3 5 8 13 21 34
# 만약 n이 4이면 반환 값은 2

# 재귀함수 
def fibo_recursion(n):
    # 기저조건
    if n == 1:
        return 0
    if n == 2:
        return 1
    # 점화식
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)

# 반복문 함수
def fibo_iteration(n):
    # 0 1 1 2 3 5 8 13 ...
    a = 0
    b = 1
    temp = 0
    count = 0
    while n != count :  
        temp = a   # temp = 0, 1, 1 , ...
        a = a + b  # a = 1, 1, 2 ...
        b = temp  # b = 0, 1, 1, ..
        count += 1 
    return b  

if __name__=="__main__":
    for i in range(1, 11):  # 1, 2, ... , 10
        #결과 값은
        # 0 1 1 2 3 5 8 13 21 34
        #print(fibo_recursion(i), end="  ")
        print(fibo_iteration(i), end="  ")