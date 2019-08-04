from random import randint

def get_mid_idx(li):
    '''
    3개 숫자 중에 중간 값을 가진 인덱스 값 반환 -> index
    li = [3, 4, 1, 5, 7]
    '''
    new_li = []
    start = li[0]  
    end = li[-1]  
    mid = li[(len(li) - 1) // 2 ]
    new_li.extend([start, mid, end])
    # new_li = [3, 1, 7]
    for i in range(len(new_li) - 1):
        for j in range(len(new_li) - i - 1):
            if new_li[j] > new_li[j + 1]:
                new_li[j], new_li[j + 1] = new_li[j + 1], new_li[j]
    # new_li = [1, 3, 7]
    return li.index(new_li[1])


def quick_sort(li):
    # 기저조건  base case
    if len(li) <= 1:
        return li

    # 점화식 recursion case
    left_idx = 0
    right_idx = len(li) - 1
    pivot = li[(len(li) - 1) // 2] 

    while left_idx <= right_idx:
        while li[left_idx] < pivot:
            left_idx += 1
        while li[right_idx] > pivot:
            right_idx -= 1

        if left_idx <= right_idx:
            li[left_idx], li[right_idx] = li[right_idx], li[left_idx]   
            left_idx += 1
            right_idx -= 1
        else:
            break
    left = li[:left_idx]  
    right = li[left_idx:]   

    li[:len(li)] = quick_sort(left) + quick_sort(right)    
    return li
    
if __name__ == "__main__":
    while True:
        num_data = int(input('데이터 개수(종료: 0): '))
        if not num_data:
            break
        li = [randint(1, 100) for _ in range(num_data)]
        print(li)
        quick_sort(li)
        print(li)
    

    
        

    



