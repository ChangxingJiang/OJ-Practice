class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.stack.append(x)
        else:
            min_val = self.stack[-1]
            self.stack.append(x)
            self.stack.append(min(min_val, x))

    def pop(self) -> None:
        self.stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-2]

    def getMin(self) -> int:
        return self.stack[-1]


if __name__ == "__main__":
    m = MinStack()
    m.push(-2)
    m.push(0)
    m.push(3)
    print(m.getMin())  # -2
    print(m.pop())  # 3
    print(m.top())  # 0
    print(m.getMin())  # -2
