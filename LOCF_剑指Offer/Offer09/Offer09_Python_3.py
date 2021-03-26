class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else -1


if __name__ == "__main__":
    obj = CQueue()
    obj.appendTail(3)
    print(obj.deleteHead())  # 3
    print(obj.deleteHead())  # -1

    obj = CQueue()
    print(obj.deleteHead())  # -1
    obj.appendTail(5)
    obj.appendTail(2)
    print(obj.deleteHead())  # 5
    print(obj.deleteHead())  # 2
