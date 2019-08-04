num = int(input("입력하실 학생 수는 몇명인가요? : "))
score_dic = {}
for _ in range(num):
    name = input("학생 이름을 입력하세요 : ")
    score = float(input("점수를 입력하세요 : "))
    if score in score_dic:
        score_dic[score].append(name)
    else:
        score_dic[score] = [name]

score_list = []
for score in score_dic:
    score_list.append([score, score_dic[score]])
score_list.sort()

for i in range(len(score_list)):
    result = score_list[i][1]
    result.sort()

print(score_list)
