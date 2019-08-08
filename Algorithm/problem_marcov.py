# def fibo(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fibo(n-2) + fibo(n-1)
#
# # Memoization (함수 입력값이 같다면 출력값 또한 같다는 전제가 있어야 한다.)
# cache = [None for _ in range(300)]
# cache[1] = 0
# cache[2] = 1
# def fibo(n):
#     if cache[n] != None:
#          return cache[n]
#     return fibo(n-1) + fibo(n-2)
#
# for i in range(1, 10):
#     print(fibo(i), end="  ")


# 탈옥수가 검문을 피해 마을과 마을 사이를 돌아다니고 있다.
# 탈옥수는 탈출 당일 인접한 마을에 숨었다.
# d일이 지났을 때 각 마을에 숨어있을 확률을 구하시오.
# 알고리즘 문제해결전략 1권 p.269

n = 5
d = 2
start = 0
connected = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

deg = [3, 2, 1, 1, 1]

# v 마을에 있을 때, days일이 지난 후 t 마을에 탈옥수가 있을 확률
def solve(v, days):
    # base case
    if days == d:
        return 1.0 if v==t else 0.0

    # 이미 계산된 값이 cache에 있다면 그 값을 반환
    if cache[v][days] != None:
        return cache[v][days]

    # 반환값을 계산해서 반환
    cache[v][days] = 0.0
    for i in range(n):
        if connected[v][i]:
            cache[v][days] += solve(i, days+1)/deg[v]
    return cache[v][days]


prob = []
for t in range(n):
    cache = [[None for _ in range(30)] for _ in range(10)]
    prob.append(solve(0, 0))

print(prob)