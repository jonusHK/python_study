from functools import reduce
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    particular_score = student_marks[query_name]
    avrg_score = reduce(lambda a, b: a + b, particular_score) / len(particular_score)

    print("%0.2f" % avrg_score)