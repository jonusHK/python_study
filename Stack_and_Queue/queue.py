# adapter pattern
# 내부에서 사용하는 구현체가 있는데 
# 상호 작용하는 객체와 인터페이스가 맞지 않을 때
# 인터페이스를 맞춰주는 클래스
class Queue:
    def __init__(self):
        # 내부 구현체
        self.container = list()

    def empty(self):
        if len(self.container):
            return False
        return True

    def enqueue(self, data):
        self.container.append(data)

    def dequeue(self):
        return self.container.pop(0)

    def peek(self):
        return self.container[0]

    def __str__(self):
        return f'{self.container}'

if __name__ == "__main__":
    # 테스트 코드
    queue = Queue()
    print(queue.empty())
    print(queue.enqueue(5))
    print(queue)
    print(queue.peek())
    print(queue.dequeue())
    print(queue)
    
    