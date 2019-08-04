from lstack import LStack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def empty(self):
        if not self.head:
            return True
        return False

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next =self.head
        self.head = new_node
    
    def traverse(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

class Position:
    def __init__(self, row, col, dir):
        self.row = row   
        self.col = col
        self.dir = dir

class MazeSolver:
    direction = ((-1, 0), (-1, 1), (0, 1), 
    (1, 1), (1, 0), (1, -1), 
    (0, -1), (-1, -1))
    def __init__(self, maze):
        self.maze = maze
        # 출구 행, 열
        '''
        maze = [
		[0, 1, 1, 0, 0],
		[1, 0, 0, 1, 1],
		[0, 1, 1, 0, 1],
		[0, 1, 0, 1, 1],
		[1, 1, 0, 0, 0],
        ]
        '''
        self.EXIT_ROW = len(maze)  
        self.EXIT_COL = len(maze[0])

        # to do : 최외곽을 1로 된 벽 생성
        for row in maze:  # for i in li:   li = [1, 2, 3]
            row.insert(0, 1)
            row.append(1)
        
        added_row = [1 for _ in range(self.EXIT_COL + 2)]
        maze.insert(0, added_row)
        maze.append(added_row)
        '''
        maze = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 0 ,1],
        [1, 0, 1, 1, 0, 1, 1],
		[1, 0, 1, 0, 1, 1, 1],
		[1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
        ]

        '''
        self.path = LinkedList()

    def get_path(self):
        stack = LStack()
        mark = []

        # mark를 0으로 가득찬 실제 미로 크기의 이중? 리스트로 만든다.
        '''
        mark = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        ]
        '''
        for _ in range(self.EXIT_ROW + 2):
            mark.append([0 for _ in range(self.EXIT_COL + 2)])
        row = None; col = None; dir = None;
        next_row = None; next_col = None;
        found = False  # 미로 마지막 지점으로 갔다면 True 로 변경

        # 미로의 시작점(1, 1)
        mark[1][1] = 1
        '''
        mark = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        ]

        maze = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 1],
		[1, 0, 1, 0, 1, 1, 1],
		[1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
        ]
        '''
        # 첫 시작 위치를 스택에 push
        stack.push(Position(1, 1, 2))
        # stack.top.data.dir
        # 스택이 비었다면 --> 목적지로 가는 경로 없다
        while not stack.empty() and not found: 
            pos = stack.pop()
            col = pos.col
            row = pos.row
            dir = pos.dir
            while dir < 8 and not found:
                next_row = row + self.direction[dir][0]
                next_col = col + self.direction[dir][1]
                if next_row == self.EXIT_ROW and next_col == self.EXIT_COL: # 마지막 지점을 찾은 경우
                    found = True
                    stack.push(Position(row, col, dir))
                    stack.push(Position(self.EXIT_ROW, self.EXIT_COL, 0))
                elif self.maze[next_row][next_col] == 0 and \
                    mark[next_row][next_col] == 0: # 통로를 만난 경우
                    mark[next_row][next_col] = 1
                    stack.push(Position(row, col, dir))
                    row = next_row
                    col = next_col
                    dir = 0
                else: # 벽을 만난경우, mark 1을 만난경우
                    dir += 1        
        
        if found:
            while not stack.empty():
                self.path.add(stack.pop())
        else:
            print('there is no path in this maze!')

    def print_path(self):
        g = self.path.traverse()
        for node in g:
            print("({}, {})".format(node.data.row, node.data.col))

    def show_maze(self):
        print('   ', end='')
        for i in range(self.EXIT_ROW+2):
            print(' ' + str(i) + ' ', end='')
        print()

        for i in range(self.EXIT_ROW+2):
            print(' ' + str(i) + ' ', end='')

            for j in range(self.EXIT_COL+2):
                if self.maze[i][j] == 0:
                    print(' O ', end='')
                else:
                    print(' # ', end='')
            print()
        print()

    def show_path(self):
        path_set = set()
        g = self.path.traverse()
        for node in g:
            path_set.add((node.data.row, node.data.col))
        
        print('   ', end='')
        for i in range(self.EXIT_ROW+2):
            print(' ' + str(i) + ' ', end='')
        print()

        for i in range(self.EXIT_ROW+2):
            print(' ' + str(i) + ' ', end='')

            for j in range(self.EXIT_COL+2):
                if (i, j) in path_set:
                    print(' P ', end='') 
                elif self.maze[i][j] == 0:
                    print(' O ', end='')
                else:
                    print(' # ', end='')
            print()
        print()

if __name__ == "__main__":
    maze = [
		[0, 1, 1, 0, 0],
		[1, 0, 0, 1, 1],
		[0, 1, 1, 0, 1],
		[0, 1, 0, 1, 1],
		[1, 1, 0, 0, 0],
    ]

    maze_solver = MazeSolver(maze)
    maze_solver.show_maze()
    maze_solver.get_path()
    maze_solver.print_path()
    maze_solver.show_path()    