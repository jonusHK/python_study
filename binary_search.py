def binary_search(li, target):
    start = 0
    end = len(li) - 1
    while start <= end:
        mid = (start + end) // 2
        if li[mid] == target:
            return mid
        elif li[mid] > target :
            end = mid - 1
        else:
            start = mid + 1
    return None

li = [1, 2, 3, 6, 7, 10]
print(binary_search(li, 10))


