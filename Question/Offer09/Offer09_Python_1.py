from queue import LifoQueue


class CQueue:

    def __init__(self):
        self.stack = LifoQueue()

    def appendTail(self, value: int) -> None:
        self.stack.put(value)

    def deleteHead(self) -> int:
        if self._is_empty():
            return -1
        else:
            temp = LifoQueue()
            while self.stack.qsize():
                temp.put(self.stack.get())

            ans = temp.get()
            while temp.qsize():
                self.stack.put(temp.get())

            return ans

    def _is_empty(self):
        return self.stack.qsize() == 0


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
