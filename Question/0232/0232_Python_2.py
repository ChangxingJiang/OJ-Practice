class MyQueue:

    def __init__(self):
        self.stark = []

    def push(self, x: int) -> None:
        self.stark.append(x)

    def pop(self) -> int:
        return self.stark.pop(0)

    def peek(self) -> int:
        return self.stark[0]

    def empty(self) -> bool:
        return len(self.stark) == 0


if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())
