# traversal (순회)
# 재방문 없이 어떤 자료구조의 모든 데이터(노드) 방문하는 것
class Stack:
    def __init__(self):
        self.container=list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

from queue import Queue
# stack 모듈 지원안하면서 queue는 모듈 지원하는 이유
# stack은 append()와 pop()을 통해 성능좋게 만들 수 있으나,
# queue는 pop(0)할 경우, 성능이 상당히 안좋아진다. --> 동적 배열의 단점

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 재귀함수 이용한 전위순회
def preorder(node):
    # base case
    if not node:
        return
    # 방문
    print(node.data, end="  ")
    # 왼쪽 자식
    preorder(node.left)
    # 오른쪽 자식
    preorder(node.right)

# 재귀함수 이용한 중위순회
def inorder(node):
    if not node:
        return

    inorder(node.left)
    print(node.data, end="  ")
    inorder(node.right)

# 재귀함수 이용한 후위순회
def postorder(node):
    if not node:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data, end="  ")

# while문 이용한 전위순회
def iter_preorder(cur):
    # 1. 처음에 cur.data 출력 및 stack에 쌓는다
    # 2. 왼쪽 자식이 있으면 계속 stack에 push하고, 없으면 pop 시킨 뒤,
    # 3. 부모 노드로 cur 이동하여 cur의 오른쪽 자식이 있으면 stack에 push하고
    # 4. 없으면, pop시킨다.
    # 2번 부터 반복
    s = Stack()

    while True:
        while cur:
            # 방문
            print(cur.data, end="  ")
            s.push(cur)
            cur = cur.left
        if s.empty():
            break
        cur = s.pop()
        cur = cur.right

# while문 이용한 중위순회
def iter_inorder(cur):
    s = Stack()

    while True:
        while cur:
            s.push(cur)
            cur = cur.left
        if s.empty():
            break
        cur = s.pop()
        # 방문
        print(cur.data, end="  ")
        cur = cur.right

# while문 이용한 후위순회
def iter_postorder(cur):
    # 1. 스택 1, 2 생성하고,
    # 2. 처음 노드 stack에 push하고,
    # 3. 스택1이 비어있지 않는 동안, 스택1 왼쪽, 오른쪽 자식있으면 스택1에 push하고 pop된것을 스택2에 push하고,
    # 4. 없으면, pop시킨 값을 스택2에 push한다.
    # 5. 스택1 비어있다면, break로 빠져나와 s2 스택 비어있을 때까지 pop하여 print한다.
    s1 = Stack()
    s2 = Stack()

    s1.push(cur)
    while not s1.empty():
        cur = s1.pop()
        if cur.left:
            s1.push(cur.left)
        if cur.right:
            s1.push(cur.right)
        s2.push(cur)

    while not s2.empty():
        cur = s2.pop()
        print(cur.data, end="  ")

# while문 이용한 레벨순회
def levelorder(cur):
    # queue에 cur 집어넣고, cur를 dequeue(get) 함과 동시에 cur.left 또는 cur.right 있으면
    # 순서대로 queue 에 enqueue(put)해주고,
    # q가 비어있지 않을 때까지 while문 반복
    q = Queue()
    q.put(cur) # q.enqueue(cur)
    while not q.empty():
        cur = q.get() # q.dequeue()
        print(cur.data, end="  ")
        if cur.left:
            q.put(cur.left)
        if cur.right:
            q.put(cur.right)


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    print("전위순회 - 재귀함수")
    preorder(n1)
    print()
    print("중위순회 - 재귀함수")
    inorder(n1)
    print()
    print("후위순회 - 재귀함수")
    postorder(n1)
    print()
    print("--------------------")
    print("전위순회 - while문")
    iter_preorder(n1)
    print()
    print("중위순회 - while문")
    iter_inorder(n1)
    print()
    print("후위순회 - while문")
    iter_postorder(n1)
    print()
    print("레벨순회 - while문")
    levelorder(n1)
    print()