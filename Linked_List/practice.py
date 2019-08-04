class Node:
    def __init__(self, data = None):
        self.__data = data
        self.__next = None

    def __del__(self):
        print(f'data of {self.__data} is deleted')
    
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
    def next(self, nxt):
        self.__next = nxt


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.d_size = 0

    def append(self, data):
        new_node = Node(data)

        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.d_size += 1

        else:
            self.tail.next = new_node
            self.tail = new_node
            self.d_size += 1

    def search_target(self, target, start = 0):
        if self.empty():
            return None
        cur = self.head
        pos = 0
        while cur:
            if cur.data == target:
                return cur, pos
            cur = cur.next
            pos += 1
        
        return None, None

    def search_pos(self, pos):
        if pos > self.size() - 1:
            return None

        cur = self.head
        count = 0
        while count < pos:
            cur = cur.next
            count += 1
        return cur.data

    def remove(self, target):
        # 데이터가 없을 때, None 반환
        if self.empty():
            return None

        cur = self.head
        # 첫 노드가 target일 때
        if cur.data == target:
            self.head = None
            self.tail = None
            self.d_size -= 1
            return cur.data

        # 첫 노드가 target이 아닐 때    
        while cur.next:
            # cur 다음 노드가 target
            if cur.next.data == target:
                # target이 tail일 때
                if cur.next == self.tail:
                    self.tail = cur
                    self.d_size -= 1
                    return cur.next.data
                # target이 tail 이전에 있을 때
                cur.next = cur.next.next
                self.d_size -= 1
                return target
            # cur 다음 노드가 target이 아닐 때
            else:
                cur = cur.next

        return None

    def empty(self):
        if self.d_size == 0:
            return True
        return False

    def size(self):
        return self.d_size

    def __str__(self):
        return f'head: {self.head.data}, tail: {self.tail.data}'

def show_list(sll):
    cur = sll.head
    for _ in range(sll.size()):
        print(cur.data, end = " ")
        cur = cur.next

if __name__ == "__main__":
    test_data = SingleLinkedList()
    test_data.append(1)
    test_data.append(2)
    test_data.append(3)
    test_data.append(4)
    test_data.append(5)

    print(test_data)

    test_data.remove(3)
    test_data.remove(3)
    test_data.remove(3)
    show_list(test_data)
    print('')