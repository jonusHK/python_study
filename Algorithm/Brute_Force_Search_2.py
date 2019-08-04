'''
boardcover
HxW의 보드가 검은색과 흰색으로 채워져 있다.
모든 흰칸을 L자 모양의 흰색 블록으로 덮고 싶다.
블록은 회전 가능하지만 겹치거나 검은색을 침범하거나 밖으로 나가서는 안된다.
보드가 있을 때 이를 덮는 방법의 수를 계산하는 프로그램을 만드시오
알고리즘 문제해결 전략 p.159 게임판 덮기
'''

# Height = 8
H = 8
# Width = 10
W = 10
board = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

cases = [
    # [y, x]
  [[1, 0], [0, 1], [0, 0]],
  [[0, 1], [1, 1], [0, 0]],
  [[1, 0], [1, 1], [0, 0]],
  [[1, 0], [1, -1], [0, 0]]
]

# (y, x) 위치가 보드를 벗어났는지를 판단하는 함수
def out_range(y, x):
  if (y < 0  or x < 0 or H <= y or W <= x):
      return True
  return False

# (y, x)에 c 타입의 블록을 넣는 함수
def put(y, x, c):
  # c(for c in cases에서의 c) : 블록 타입
  ret = True
  # c = [[1, 0], [0, 1], [0, 0]]
  for point in c:
      # point = [1, 0] // [0, 1] // [0, 0]
      _y = y + point[0] # _y = y(1) + 1 = 2 // y(1) + 0 = 1 // y(1) + 0 = 1
      _x = x + point[1] # _x = x(1) + 0 = 1 // x(1) + 1 = 2 // x(1) + 0 = 1
      if out_range(_y, _x):
          ret = False
      else:
          board[_y][_x] += 1
          if board[_y][_x] > 1:
              ret = False

  return ret

# (y, x)에서 c 타입의 블록을 빼는 함수
def get(y, x, c):
  for point in c:
      _y = y + point[0]
      _x = x + point[1]
      if out_range(_y, _x):
          continue
      else:
          board[_y][_x] -= 1

def solve():
  # base case
  fx = fy = None
  # for i in range(8):
  for i in range(H):
      # for j in range(10):
      for j in range(W):
          if board[i][j] == 0:
              # board[1][1] == 0
              # fy = 1
              fy = i
              # fx = 1
              fx = j
              break

      if fx != None:
          break

  if fx == None:
      return 1

  ret = 0
  # put()이 존재하지 않으면(=블록 들어갈 공간 없으면) return 0
  for c in cases:
      # put(1, 1, cases[0]):
      if put(fy, fx, c):
          # ret += solve()
          ret += solve()
      get(fy, fx, c)

  return ret

print(solve())