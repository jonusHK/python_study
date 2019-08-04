import random
import time

def get_pivot_index(li, start, mid, end):
    """
    get_pivot_index(li, start, mid, end) -> index
    리스트의 맨 처음 값, 가운데 값, 마지막 값 중에서
    중간 값을 가진 인덱스를 반환한다!!
    """
    # bubble sort 
    index = start, mid, end  
    li_sort = [li[v] for v in index]    
    for i in range(len(li_sort) - 1):
        for j in range(len(li_sort) - 1 - i):
            if li_sort[j] > li_sort[j + 1]:
                li_sort[j], li_sort[j + 1] = li_sort[j + 1], li_sort[j]  
    for i in range(len(li)):
        if li[i] == li_sort[1]:
            pivot_index = i

    return(pivot_index)


def quick_sort(li, start, end):
    #base case
    if start >= end:
        return

    left = start   
    right = end
    mid = (start + end) // 2
    pivot_index = get_pivot_index(li, start, mid, end)
    li[pivot_index], li[mid] = li[mid], li[pivot_index]
    pivot = li[mid]
    # [2, 6, 4, 6, 7, 7, 7]
    while left <= right:  
        while li[left] < pivot:  
            left += 1
        
        while li[right] > pivot:
            right -= 1

        if left <= right:
            li[left], li[right] = li[right], li[left]
            left += 1
            right -= 1

    quick_sort(li, start, right)
    quick_sort(li, left, end)

if __name__ == "__main__":
    while True:
        num_data = int(input("데이터 개수(종료 : 0): "))
        if not num_data:
            break
        
        data = [random.randint(1, 100) for _ in range(num_data)]
        print(data)
        quick_sort(data, 0, len(data) - 1)
        print(data)