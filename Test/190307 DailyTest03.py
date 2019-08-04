'''
2. 다음 코드에서 *b에 담겨있는 값을 적으세요.
   numbers = [1, 2, 3, 4, 5, 6]
   a, *b, c = numbers
   Ans> [2, 3, 4, 5]
   
3. 출력 값이 "1 / 1 / 2 / 3 / 5 / 8 / 13 / 21 / 34 / 55"가 되는 함수를 구현하세요.
Ans>
def fibonacci(n):
   #base case
   if n <= 1:
      return 1

   #recursive case
   return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
   print(fibonacci(i), end = " / ")

1*1, (1*1)*2, ((1*1)*2)*3

4. 출력값이 "1 2 6 24 120" 이 되는 함수를 구현하세요.
Ans>
def func(n):
   #base case
   if n == 0:
      return 1
   #recursive case 
   return func(n - 1) * n

for i in range(1, 6):
   print(func(i), end = " ")

5. 기저 조건이 없는 재귀 함수, 즉 무한 루프를 도는 함수를 실행할 때 발생하는 현상을 스택을 이용해 간단히 설명하세요. 
Ans> 함수 호출 시, 스택 프레임이 쌓이게 되는데 기저 조건(탈출 조건)이 없는 재귀함수의 경우, 함수를 무한대로 호출하게 되고 이는 스택 프레임이 무한대로 쌓게 되는 결과를 초래합니다. 기저 조건(탈출 조건)이 있음으로써, 마지막 함수(스택 맨 위)에서 일정 값이 리턴되어 차례대로 스택 프레임이 사라지게 됩니다.   
'''