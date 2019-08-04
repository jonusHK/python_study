class Node:
    def __init__(self, data = None):
        self.__data = data
        self.__prev = None
        self.__next = None
    
    def __del__(self):
        print(f'deleted : [{self.__data}]')

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, prev):
        self.__prev = prev

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, nxt):
        self.__next = nxt

class DoubleLinkedList:
    def __init__(self):
        # 더미 생성 시점
        self.head = Node()
        self.tail = Node()
        self.d_size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def empty(self):
        if self.d_size == 0:
            return True
        return False

    def size(self):
        return self.d_size

    def add_first(self, data):
        new_node = Node(data)
        # new_node를 연결한다.
        new_node.next = self.head.next
        new_node_prev = self.head
        # 리스트 입장에서 연결
        self.head.next.prev = new_node
        self.head.next = new_node

        self.d_size += 1
        
    def add_last(self, data):
        new_node = Node(data)
        new_node_prev = self.tail.prev
        new_node_next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.d_size += 1

    def insert_after(self, data, node):
        new_node = Node(data)

        # new_node 연결
        new_node.next = node.next
        new_node.prev = node

        # 리스트 관점에서 연결
        node.next.prev = new_node
        node.next = new_node

        self.d_size += 1
        

    def insert_before(self, data, node):
        new_node = Node(data)

        # new_node 연결
        new_node.prev = node.prev
        new_node.next = node

        # 리스트 관점에서 연결
        node.prev.next = new_node
        node.prev = new_node
        
        self.d_size += 1

    def search_forward(self, target):
        cur = self.head.next
        while cur is not self.tail:    
            if cur.data == target:
                return cur
            cur = cur.next
        return None

    def search_backward(self, target):
        cur = self.tail.prev
        while cur is not self.head:
            if cur.data == target:
                return cur
            cur = cur.prev
        return None

    # 편의 함수 - generator
    def traverse(self, start = True):
        if start:
            # 리스트의 첫 데이터부터 순회!
            cur = self.head.next
            # a = 'i am'
            # b = 'i am'
            # a == b : True
            # a is b : False
            while cur is not self.tail:
                yield cur
                cur = cur.next

            
        else:
            # 리스트의 마지막 데이터부터 순회!
            cur = self.tail.prev
            while cur is not self.head:
                yield cur 
                cur = cur.prev    
    
    def delete_first(self):
        if self.empty():
            return 
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
            
        self.d_size -= 1
        
    def delete_last(self):
        if self.empty():
            return
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        
        self.d_size -= 1

    def delete_node(self, node):
        if self.search_backward(node):
            node.prev.next = node.next
            node.next.prev = node.prev

            self.d_size -= 1
            

def show_list(dlist):
    g = dlist.traverse()

    for node in g:
        print(node.data, end = " ")
    print()

if __name__ == "__main__":
    dlist = DoubleLinkedList()
    dlist.add_first(1)
    dlist.add_first(2)
    dlist.add_first(3)
    dlist.add_first(4)
    dlist.add_first(5)
    # generator 객체
    show_list(dlist)

    searched_data = dlist.search_backward(3)
    if searched_data:
        dlist.insert_before(15, searched_data)
    else:
        print('기준 노드가 없습니다. 다시 확인하세요!')
    
    show_list(dlist)
    dlist.delete_first()
    show_list(dlist)

    del_data = dlist.search_forward(15)
    if del_data:
        dlist.delete_node(del_data)
        del_data = None
    else:
        print('기준 노드가 없습니다. 다시 확인하세요!')

    show_list(dlist)

    print('*' * 100)