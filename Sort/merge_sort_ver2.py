# 과제 문제 풀이.


# 한개가 될때까지 계속 반으로 쪼개

# 쪼개진 값의 인덱스0 과 인덱스 1의 값을 비교 후 짝은걸 앞으로 올린다.
import random

def merge(li, start, mid, end):
    '''
    쪼개진 두 개 리스트 조각에서
    left_idx, right_idx 를 비교해서
    작은 값을 올리면서 다음 칸으로 이동
    둘 중 하나가 범위를 벗어날 때
    '''
    left_idx=start
    right_idx=mid+1
    temp=[]
    # 둘중 하나가 레인지를 벗어나지 않을때
    # 전체 바에 하나씩 체워 나가는것
    while left_idx <= mid and right_idx <= end:
        if li[left_idx] < li[right_idx]:
            temp.append(li[left_idx])
            left_idx += 1

        else:
            temp.append(li[right_idx])
            right_idx += 1        
    # l이 범위를 벗어나지 않았다면    
    while left_idx <= mid: 
        temp.append(li[left_idx])
        left_idx += 1
        
    # r 이 범위를 벗어나지 않았다면
    while right_idx <= end:
        temp.append(li[right_idx])
        right_idx += 1

    li[start:end + 1] = temp

def merge_sort(li, start, end):
    # base case
    if start >= end:
        return

    mid = (start + end) // 2
    merge_sort(li, start, mid)
    merge_sort(li, mid + 1, end)

    merge(li, start, mid, end)

if __name__ == '__main__':
    while True:
        num_data=int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        data=[random.randint(1, 100) for _ in range(num_data)]
        print(data)
        merge_sort(data, 0, len(data) - 1)
        print(data)