"""
head와 tail을 0번 인덱스로

1. 크기가 정해져 있는 배열(list)
2. head, tail
3. empty --> head == tail
4. full --> tail + 1 == head
5. tail --> 마지막 데이터의 다음을 가르킨다.

ADT -> Abstract Data Type(추상 자료형)
"""

class CQueue:
    MAXSIZE = 10
    def __init__(self):
        self.__container = [None for _ in range(CQueue.MAXSIZE+1)]
        self.__head = 0
        self.__tail = 0

    def is_empty(self):
        if self.__head == self.__tail:
            return True
        return False

    def is_full(self):
        next = self.__step_forward(self.__tail)
        if next == self.__head:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            raise Exception("The queue is full")
        self.__tail = self.__step_forward(self.__tail)
        self.__container[self.__tail] = data

    def dequeue(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        self__head = self.__container[self.__head + 1]
        self.__head = self.__step_forward(self.__head)
        return self__head

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        return self.__container[self.__head + 1]

    # 편의 함수
    def __step_forward(self, x):
        x += 1
        if x >= CQueue.MAXSIZE+1:
            x = 0
        return x

    def __str__(self):
        return str(self.__container)

if __name__ =="__main__":
    cq = CQueue()

    for i in range(9+1):
        cq.enqueue(i + 1)
        print(f"enqueue: {i+1}")

    for i in range(5+1):
        print("dequeue: ", cq.dequeue())


    print("tail: ", cq._CQueue__tail)
    print("head: ", cq._CQueue__head)
    print("peek: ", cq.peek())
    print("container: ", cq)
    print("is full? ", cq.is_full())
    print("is empty? ", cq.is_empty())
