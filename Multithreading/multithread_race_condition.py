import threading
# race condition
# 해결책!!!!!
# mutual exclusion : 상호 배제
# 공유 자원
g_num = 0
lock = threading.Lock()

def thread_main():
    global g_num
    
    # critical section
    # 스레드가 공유자원에 접근은 괜찮은데
    # 공유 자원을 수정하려고 하는 코드
    lock.acquire()
    for _ in range(100000):
        g_num += 1
    lock.release()

threads = []

for i in range(50):
    threads.append(threading.Thread(target = thread_main))

for th in threads:
    th.start()

for th in threads:
    th.join()

print(f'g_num : {g_num}')