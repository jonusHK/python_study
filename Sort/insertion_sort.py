# insertion sort
from random import randint
# li = [4, 5, 3, 2, 1]
def insertion_sort(li):
    for i in range(1, len(li)):  # i = 1, 2, 3, 4
        key = li[i]  # key = 5
        j = i - 1  # i = 3, j = 2
        while j >= 0:
            if li[j] > key:
                li[j + 1] = li[j]
            else:
                break
            j -= 1
        li[j + 1] = key
    return li

while True:
    num_data = int(input('데이터 개수(종료 : 0) :'))
    if not num_data:
        break
    
    li = [randint(1, 100) for _ in range(num_data)]
    print(li)
    result = insertion_sort(li)
    print(result)



