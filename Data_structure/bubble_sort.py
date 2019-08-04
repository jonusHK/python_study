from random import randint

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



if __name__ == "__main__":
    arr = [randint(0, 1000) for _ in range(5)]
    bubble_sort(arr)
    print(arr)