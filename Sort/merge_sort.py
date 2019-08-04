from random import randint

def merge(left, right):
    '''
    쪼개진 두 리스트 조각에서 
    left_idx, right_idx 비교
    작은 값을 올리면서 다음 칸으로 이동
    둘 중 하나가 범위를 벗어날 때
    '''
    # left = [1, 2, 7, 8]   
    # right = [4, 5, 6, 9]
    new_li = []   # new_li = [1, 2, 4, 5, 6, 7, 8, 9]
    i = 0
    j = 0
    while i <= len(left) - 1 and j <= len(right) - 1:
        if left[i] <= right[j]:
            new_li.append(left[i])
            i += 1
        else:
            new_li.append(right[j]) 
            j += 1
    if i == len(left):
        new_li = new_li + right[j:]
    if j == len(right):
        new_li = new_li + left[i:]

    return new_li



def merge_sort(li):
    # base case
    if len(li) == 1:
        return li
    # li = [8, 7, 2, 1, 4, 5, 6, 9]
    # recursion case
    mid = (len(li) - 1) // 2
    left = li[:mid + 1]   # left = [8, 7, 2, 1]
    right = li[mid + 1:]   # right = [4, 5, 6, 9]

    li[:len(li)] = merge(merge_sort(left), merge_sort(right)) 
    return li
    

if __name__ == "__main__":
    num_data = int(input('데이터 개수(종료: 0): '))
    li = [randint(1, 100) for _ in range(num_data)]
    merge_sort(li)
    print(li)