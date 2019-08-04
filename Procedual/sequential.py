# 2019.03.19 화요일

from openpyxl import load_workbook
from functools import reduce
from math import sqrt
# raw_data : 학생 : key, 점수 : value --> dictionary
raw_data = {}
wb = load_workbook('class_2_3.xlsx')
ws = wb.active
g = ws.rows
for name_cell, score_cell in g:
   raw_data[name_cell.value] = score_cell.value

# average : 학생 평균
scores = tuple(raw_data.values())
avrg = reduce(lambda x, y : x + y, scores) / len(scores)

# variance : 학생 점수 분산
var = reduce(lambda result, a : result + (a - avrg) ** 2, scores, 0) / len(scores)

# std_dev : 표준편차
std_dev = sqrt(var)

print("평균:{}, 분산:{}, 표준편차:{}".format(avrg, var, std_dev))

if avrg < 50 and std_dev > 20:
    print('성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.')
elif avrg > 50 and std_dev > 20:
    print('성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!')
elif avrg < 50 and std_dev < 20:
    print('학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!')
elif avrg > 50 and std_dev < 20:
    print('성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.')