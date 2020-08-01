class MyStack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.stack.pop(self.size)

    def top(self) -> int:
        if self.size != 0:
            return self.stack[self.size - 1]

    def empty(self) -> bool:
        return self.size == 0


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.pop())
    obj.empty()
