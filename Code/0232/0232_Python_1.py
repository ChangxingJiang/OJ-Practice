from queue import LifoQueue


class MyQueue:

    def __init__(self):
        self.stark = LifoQueue()

    def push(self, x: int) -> None:
        self.stark.put(x)

    def pop(self) -> int:
        temp = LifoQueue()
        for _ in range(self.stark.qsize() - 1):
            temp.put(self.stark.get())

        ans = self.stark.get()

        for _ in range(temp.qsize()):
            self.stark.put(temp.get())
        return ans

    def peek(self) -> int:
        if self.stark.qsize() != 0:
            temp = LifoQueue()
            for _ in range(self.stark.qsize() - 1):
                temp.put(self.stark.get())

            ans = self.stark.get()

            self.stark.put(ans)
            for _ in range(temp.qsize()):
                self.stark.put(temp.get())

            return ans

    def empty(self) -> bool:
        return self.stark.qsize() == 0


if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())
