class Node:
    def __init__(self, data = None):
        self.__data = data
        self.__link = None
    
    # 소멸자
    # 객체가 사라지기 전에
    # 반드시 한번 호출하는 것을
    # 보장한다!!
    def __del__(self):
        print(f'node[{self.__data}] deleted!!')

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, link):
        self.__link = link

class SLinkedList:
    def __init__(self):
        self.head = None
        self.d_size = 0

    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def add(self, data):
        new_node = Node(data)
        new_node.link = self.head
        self.head = new_node
        
        self.d_size += 1

    def search(self, target):
        cur = self.head
        while cur:
            if cur.data == target:
                return cur
            else:
                cur = cur.link
        return cur
    def delete(self):
        if self.empty():
            return
        self.head = self.head.link
        self.d_size -= 1

    def size(self):
        return self.d_size

    def tranverse(self):
        cur = self.head

def show_list(sll):
    cur = sll.head
    for i in range(sll.size()):
        print(cur.data, end = " ")
        cur = cur.link

if __name__ == "__main__":
    sll = SLinkedList()
    sll.add(1)
    sll.add(3)
    sll.add(4)
    show_list(sll)


    target = 4
    result = sll.search(target)
    if result:
        print(f'searched data : {result.data}')
    else:
        print('there is no such data')


    print('*'*10)




