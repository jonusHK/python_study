from random import randint

# for문, while문 사용
# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         temp = arr[i]
#         j = i - 1
#         while j >= 0:
#             if arr[j] > temp:
#                 arr[j+1] = arr[j]
#             else:
#                 break
#             j -= 1
#         arr[j+1] = temp
#     return arr

# for 문 2개 사용
def insertion_sort(arr):
    n = len(arr)
    if n > 1:  
        for i in range(1, n):
            temp = arr[i]  
            for j in range(i-1, -2, -1):
                if j == -1 :
                    break
                if arr[j] > temp:
                    arr[j+1] = arr[j]
                else:
                    break
            arr[j+1] = temp

if __name__ == "__main__":
    arr = [randint(0, 1000) for _ in range(5)]
    insertion_sort(arr)
    print(arr)