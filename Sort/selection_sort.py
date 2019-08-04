from random import randint

def selection_sort(li):
    for i in range(len(li) - 1):
        min_idx = i
        for j in range(i + 1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j
        li[i], li[min_idx] = li[min_idx], li[i]

    return li

# def selection_sort(li):
#     for i in range(len(li) - 1):
#         min_idx = i
#         j = i + 1
#         while j <= len(li) - 1:
#             if li[min_idx] > li[j]:
#                 min_idx = j
#             j += 1
#         li[i], li[min_idx] = li[min_idx], li[i]

#     return li

if __name__ == "__main__":
    while True:
        num_data = int(input('데이터 개수(종료: 0): '))
        if not num_data:
            break
        li = [randint(1, 100) for _ in range(num_data)]
        print(li)
        result = selection_sort(li)
        print(result)

