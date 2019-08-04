'''
students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
'''
# 점수 기준 오름차순으로 정렬
def score_sort(list):
    for i in range(len(list)):
        j = 1
        key_first = list[i]
        key_second = list[i][1]
        while i - j >= 0 and key_second < list[i - j][1]:
                list[i - j + 1] = list[i - j]
                j += 1
        list[i - j + 1] = key_first
    return list


# 같은 점수 내에서 알파벳 순서대로 정렬
# [['Harry', 35], ['Berry', 37.21], ['Tina', 37.21], ['Harsh', 37.21], ['Akriti', 41]]
def alphabet_sort(list):
    # 같은 점수의 인덱스(start~ end) 위치 검색
    i = 0
    check = 0
    num = int(input("몇번째로 점수가 낮은 학생이 궁금한가요?: "))
    while i <= len(list) - 1:
        j = 0
        count = 0
        while i + j + 1 <= len(list) - 1 and list[i][1] == list[i + j + 1][1]:
            count += 1
            j += 1
        if count:
            # 알파벳 기준 오름차순으로 bubble sort 정렬
            for k in range(count):
                for m in range(i, i + count - k):   # range(1, 3)
                    if list[m][0] > list[m + 1][0]:
                        list[m], list[m + 1] = list[m + 1], list[m]
        # 두번째로 낮은 점수를 받은 학생의 이름 출력
        check += 1
        if check == num:
            for i in range(i, count + i + 1):
                print(list[i][0])
        i = i + count + 1
    if check < num:
        print('그런 학생은 없습니다.')

    return list


students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
score_sort(students)
alphabet_sort(students)