from random import randint

# quick sort ted edu 검색해서 동영상 볼 것

# 변수 1개 선정
def quick_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # recursive case
    left = 0
    right = len(arr) - 1
    pivot = arr[(left + right) // 2][1]

    while right >= left:
        while arr[left][1] < pivot:
            left += 1
        while arr[right][1] > pivot:
            right -= 1

        if right >= left:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    arr_left = arr[:left]
    arr_right = arr[left:]

    arr[:len(arr)] = quick_sort(arr_left) + quick_sort(arr_right)
    return arr

# 변수 3개 선정
def quick_sort(arr, start, end):  # start : arr의 시작위치, end : arr의 끝 위치
    # base case
    if start >= end:
        return
    # recursive case
    left = start
    right = end

    pivot = arr[(left + right) // 2]

    # partition
    # left와 right가 교차하기 전이라면,
    while right >= left:
        # left가 언제 멈춰야 하나?
        while arr[left] < pivot:
            left += 1
        
        while arr[right] > pivot:
            right -= 1

        # left와 right가 교차하지 않았다면
        # 교환
        if right >= left:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    
    quick_sort(arr, start, right)
    quick_sort(arr, left, end)



if __name__ == "__main__":
    arr = [randint(0, 1000) for _ in range(5)]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
