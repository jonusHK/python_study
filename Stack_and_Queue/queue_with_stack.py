from stack import Stack
# first stack -> second stack : 한번 !!

class Queue:
    def __init__(self):
        self.first = Stack()
        self.second = Stack()


    def empty(self):
        # if len(self.container):
        #     return False
        # return True
        if self.first.empty() and self.second.empty():
            return True
        return False


    def enqueue(self, data):
        self.first.push(data)   

    def dequeue(self):
        if self.empty():       
            return None

        if self.second.empty():
            while not self.first.empty():
                self.second.push(self.first.pop())

        return self.second.pop()
        
    def peek(self):
        # return self.container[0]
        if self.empty():
            return None

        if self.second.empty():
            while not self.first.empty():
                self.second.push(self.first.pop())

        return self.second.peek()


if __name__ == "__main__":
    # 테스트 코드
    queue = Queue()
    print(queue.empty())
    print(queue.enqueue(1))
    print(queue.enqueue(2))
    print(queue.peek())
    
    

