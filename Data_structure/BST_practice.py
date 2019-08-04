class TreeNode:
    def __init__(self, key):
        self.__key = key
        self.__left = None
        self.__right = None

    # getter
    @property
    def key(self):
        return self.__key

    # setter
    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

class BST:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    def preorder(self, cur):
        if not cur:
            return
        print(cur.key, end="  ")
        self.preorder(cur.left)
        self.preorder(cur.right)



    def insert(self, key):
        new_node = TreeNode(key)

        cur = self.__root

        if not cur:
            self.__root = new_node
            return

        while True:
            parent = cur
            if key < cur.key:
                cur = cur.left
                if not cur:
                    parent.left = new_node
                    return
            else:
                cur = cur.right
                if not cur:
                    parent.right = new_node
                    return


    def search(self, target):
        cur = self.__root
        while cur:
            if cur.key == target:
                return cur.key
            elif target < cur.key:
                cur = cur.left
            elif target > cur.key:
                cur = cur.right
        return None

    def delete(self, target):
        self.__root = self.__delete_recursion(self.__root, target)

    # 재귀함수
    # delete : 자료구조에서 특정 데이터 삭제 후, 반환안할 때 사용
    # remove : 자료구조에서 특정 데이터 삭제 후, 반환할 때 사
    def __delete_recursion(self, cur, target):
        # base case
        if not cur:
            return None
        elif target < cur.key:
            cur.left = self.__delete_recursion(cur.left, target)
        elif target > cur.key:
            cur.right = self.__delete_recursion(cur.right, target)
        else:
            # 삭제 노드가 리프 노드인 경우
            if not cur.left and not cur.right:
                cur = None
            # 삭제 노드의 왼쪽 자식이 있는 경우
            elif not cur.right:
                cur = cur.left
            # 삭제 노드의 오른쪽 자식이 있는 경우
            elif not cur.left:
                cur = cur.right
            # 삭제 노드의 자식이 둘일 때
            else:
                # 대체 노드를 찾는다.
                rep = cur.left
                while rep.right:
                    rep = rep.right
                # 삭제 노드와 대체 노드의 키를 교환
                cur.key, rep.key = rep.key, cur.key

                cur.left = self.__delete_recursion(cur.left, rep.key)
        return cur
if __name__=="__main__":
    bst = BST()

    bst.insert(6)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(10)
    bst.insert(9)
    bst.insert(11)

    bst.preorder(bst.root)

    # 삭제노드가 리프노드일 때
    bst.delete(6)
    print()
    bst.preorder(bst.root)