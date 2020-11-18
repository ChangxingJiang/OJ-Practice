class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(x)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        if self.empty():
            return -1
        else:
            return self.stack1.pop()

    def peek(self) -> int:
        if self.empty():
            return -1
        else:
            return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0


if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())  # 1
    print(queue.pop())  # 1
    print(queue.empty())  # False
