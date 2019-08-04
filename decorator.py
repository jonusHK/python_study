from functools import wraps
import time

def benchmarker(org_func):     #어떤 함수의 실행시간 확인 --> benchmarking
    @wraps(org_func)
    def inner(*args, **kwargs):
        start = time.time()
        result = org_func(*args, **kwargs)
        elapsed = time.time() - start
        print(f'elapsed time : {elapsed: .10f}')
        return result
    return inner

def callcounter(org_func):
    g_call_num = 0
    @wraps(org_func)
    def inner(*args, **kwargs):
        nonlocal g_call_num
        g_call_num += 1
        print(f'callcounter : {g_call_num}')
        return org_func(*args, **kwargs)
    return inner

@benchmarker
@callcounter
def func(a, b):
    time.sleep(2)
    return a + b

if __name__ == "__main__":
    for _ in range(10):
        func(2, 3)