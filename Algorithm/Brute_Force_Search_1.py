'''
소풍
어떤 학교에 소풍을 간다. 학생들을 두 명씩 짝지어 행동하게 하려 한다.
서로 친구인 경우에만 짝을 지어야 한다.
서로 친구인 경우의 쌍이 주어질 때
학생들을 짝지을 수 있는 방법의 수를 구하는 프로그램을 구현하라.
데이터 개수(학생 수) n은 항상 짝수이다.
알고리즘 문제 해결 전략 1권 p.157
'''

# 학생수: n
n = 4
# 0,1,2,3번 학생이 있을 때, 서로 친구인 경우를 표시하기 위해 이중 리스트 사용
# ex. friends[0][1], friends[1][2], friends[1][3], ...
friends = [[False for _ in range(n)] for _ in range(n)]
# ex. friends[0][1] = True --> 0번과 1번이 친구
friends[0][1] = friends[1][0] = True
friends[1][2] = friends[2][1] = True
friends[2][3] = friends[3][2] = True
friends[3][0] = friends[0][3] = True
friends[0][2] = friends[2][0] = True
friends[1][3] = friends[3][1] = True

# 해당 학생이 짝이 있는 경우를 True, False 로 표시
has_pair = [False for _ in range(n)]
# 재귀에서 가장 중요한 것은 계산되는 데이터의 개수가 점점 줄어들어야 한다는 것이다.

# has_pair = [F, F, F, F]
def solve(has_pair):
  # base case
  first = None
  for i in range(n):
      # 1)has_pair[0] == False // 2)has_pair[2] == False // 3)False is not in has_pair
      if has_pair[i] == False:
          # first = 0 // first = 2
          first = i
          break

  # 3)first == None
  if first == None:
      # 3) return 1
      return 1

  ret = 0
  # 1)for stu in range(1, 4): // 2)for stu in range(3, 4)
  for student in range(first+1, n):
      if has_pair[student] == False and friends[first][student] == True:
          has_pair[student] = has_pair[first] = True
          # 1)has_pair = [T, T, F, F] // 2)has_pair = [T, T, T, T]
          ret += solve(has_pair) # 1)solve([T, T, F, F]) // 2)solve([T, T, T, T]) // 3)1 -> ret += 1 -> has_pair = [T, T, F, F] ...
          has_pair[student] = has_pair[first] = False

  return ret


print(solve(has_pair))