# 피보나치 함수를 재귀함수를 통해 구현하되
# 내부에 캐시로 사용할 자료구조를 두고
# 한번 호출되었던 값은 캐시에 저장해두었다가
# 다음번에 다시 같은 매개변수가 전달되면 
# 연산하지 않고 캐시에 저장된 값을 
# 바로 반환하도록 구현하십시오.
# 캐시로 사용할 자료구조는 리스트로 한정하며
# 리스트는 [0, 1]부터 시작합니다.
# 클로저를 이용해 구현하십시오.

# Memorization --> dynamic programming
def make_fibo():
    cache = [0, 1]
    def inner(n):
        if n > len(cache) :
            cache.append(inner(n - 2) + inner(n - 1))
        return cache[n - 1]
    return inner


# 테스트 코드는 다음과 같습니다.
if __name__=="__main__":
    fibo = make_fibo()
    for i in range(1, 11):
        print(fibo(i), end="  ")
