from queue import LifoQueue


class CQueue:
    def __init__(self):
        self.stack1 = LifoQueue()
        self.stack2 = LifoQueue()

    def appendTail(self, value: int) -> None:
        self.stack1.put(value)

    def deleteHead(self) -> int:
        if self.stack2.qsize() == 0:
            while self.stack1.qsize():
                self.stack2.put(self.stack1.get())
        return self.stack2.get() if self.stack2.qsize() else -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

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
