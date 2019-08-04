import threading

def thread_main(li, i):
    for idx in range(offset * i, offset * (i + 1)):
        li[idx] *= 2

threads = []
num_elem = 1000
num_thread = 4
offset = num_elem // num_thread

li = [i + 1 for i in range(num_elem)]

for i in range(num_thread):
    th = threading.Thread(target = thread_main, args = (li, i))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

print(li)