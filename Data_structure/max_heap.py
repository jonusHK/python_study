class Element:
    def __init__(self, key):
        self.__key = key

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, k):
        self.__key = k


class MaxHeap:
    MAX = 1024
    def __init__(self):
        self.__heapsize = 0
        self.__container = [None for _ in range(MaxHeap.MAX)]

    def __get_parent_idx(self, cur):
        return cur // 2

    def __get_left_child_idx(self, cur):
        return cur * 2

    def __get_right_child_idx(self, cur):
        return cur * 2 + 1

    def is_empty(self):
        if self.__heapsize == 0:
            return True
        return False

    def is_full(self):
        if self.__heapsize == MaxHeap.MAX:
            return True
        return False

    def push(self, key):
        if self.is_full():
            raise IndexError("The heap is full")

        self.__heapsize += 1
        cur_idx = self.__heapsize
        # cur_idx != root
        # key > container[parent].key
        par_idx = self.__get_parent_idx(cur_idx)
        while cur_idx != 1 and key > self.__container[par_idx].key:
            self.__container[cur_idx] = self.__container[par_idx]
            cur_idx = par_idx
            par_idx = self.__get_parent_idx(cur_idx)
        self.__container[cur_idx] = Element(key)

    # 편의함수
    def __get_bigger_child_idx(self, cur):
        left_child_idx = self.__get_left_child_idx(cur)

        if left_child_idx > self.__heapsize:
            return None

        elif left_child_idx == self.__heapsize:
            return left_child_idx

        else:
            left_child = self.__container[left_child_idx]
            right_child = self.__container[self.__get_right_child_idx(cur)]
            if left_child.key > right_child.key:
                return left_child_idx
            else:
                return self.__get_right_child_idx(cur)

    def pop(self):
        if self.is_empty():
            raise IndexError("The heap is empty")

        ret = self.__container[1]

        temp = self.__container[self.__heapsize]

        cur = 1

        bigger_child_idx = self.__get_bigger_child_idx(cur)

        while bigger_child_idx and \
                temp.key < self.__container[bigger_child_idx].key:
            self.__container[cur] = self.__container[bigger_child_idx]
            cur = bigger_child_idx
            bigger_child_idx = self.__get_bigger_child_idx(cur)

        self.__container[cur] = temp

        self.__heapsize -= 1

        return ret.key


    def top(self):
        if self.is_empty():
            raise IndexError("The heap is empty")

        return self.__container

if __name__ == "__main__":
    heap = MaxHeap()

    heap.push(10)
    heap.push(7)
    heap.push(8)
    heap.push(15)

    for idx in range(heap._MaxHeap__heapsize+1):
        elem = heap._MaxHeap__container[idx]
        if elem:
            print(elem.key, end="  ")
    print()

    while not heap.is_empty():
        print(heap.pop(), end="  ")
