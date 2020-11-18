class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        temp = []
        while self.stack and self.stack[-1] < val:
            temp.append(self.stack.pop())

        self.stack.append(val)

        while temp:
            self.stack.append(temp.pop())

    def pop(self) -> None:
        if not self.isEmpty():
            self.stack.pop()

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.stack[-1]

    def isEmpty(self) -> bool:
        return len(self.stack) == 0


if __name__ == "__main__":
    stack = SortedStack()
    stack.push(1)
    stack.push(2)
    print(stack.peek())  # 1
    stack.pop()
    print(stack.peek())  # 2

    stack = SortedStack()
    stack.pop()
    stack.pop()
    stack.push(1)
    stack.pop()
    print(stack.isEmpty())  # True
