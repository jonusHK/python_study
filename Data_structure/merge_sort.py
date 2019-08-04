## 방법 1) 변수 여러개
# def merge(arr, start, mid, end):  # [5, 7, 9] , [3, 4, 8]
#     left = start
#     right = mid + 1
#
#     temp = []
#
#     # 둘 중 하나라도 범위를 벗어나기 전까지
#     while left <= mid and right <= end:
#         if arr[left] >= arr[right]:
#             temp.append(arr[right])
#             right += 1
#         else:
#             temp.append(arr[left])
#             left += 1
#
#     # 만약 남아있는게 left라면,
#     # temp에 넣는다.
#     while left <= mid:
#         temp.append(arr[left])
#         left += 1
#
#
#     # 만약 남아있는게 right라면,
#     while right <= end:
#         temp.append(arr[right])
#         right += 1
#
#     arr[start:end+1] = temp
#
# def merge_sort(arr, start, end):
#     # base case
#     if start >= end:
#         return
#
#
#     mid = (start+end) // 2
#
#     # devide
#     merge_sort(arr, start, mid)
#     merge_sort(arr, mid+1, end)
#
#     # conquer
#     merge(arr, start, mid, end)


# 방법 2) 변수 1개
def merge(arr_left, arr_right):  # [5, 8, 10],  [3, 6, 7]
    left = 0
    right = 0

    temp = []

    while left <= len(arr_left)-1 and right <= len(arr_right)-1:
        if arr_left[left] >= arr_right[right]:
            temp.append(arr_right[right])
            right += 1
        else:
            temp.append(arr_left[left])
            left += 1

    while left <= len(arr_left)-1:
        temp.append(arr_left[left])
        left += 1

    while right <= len(arr_right)-1:
        temp.append(arr_right[right])
        right += 1

    return temp

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr)-1) // 2
    arr_left = arr[:mid+1]
    arr_right = arr[mid+1:]

    arr[:len(arr)] = merge(merge_sort(arr_left), merge_sort(arr_right))
    return arr




from random import randint
if __name__ == "__main__":
    arr = [randint(0, 100) for _ in range(10)]
    # merge_sort(arr, 0, len(arr)-1)
    merge_sort(arr)
    print(arr)
