class Node:
    def __init__(self, data = None):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, n):
        self.__next = n

class LStack:
    def __init__(self):
        self.top = None

    def empty(self):
        if self.top is None:
            return True
        return False

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.empty():
            return
        cur = self.top
        self.top = self.top.next
        return cur.data

    def peek(self):
        if self.empty():
            return
        return self.top

    def tranverse(self):
        cur = self.top
        while cur:
            yield cur
            cur = cur.next


if __name__ == "__main__":
    stack = LStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    

