class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = [-10000001]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.max_stack.append(max(x, self.max_stack[-1]))

    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        val = self.max_stack.pop()

        temp = [self.stack.pop()]
        while temp[-1] != val:
            self.max_stack.pop()
            temp.append(self.stack.pop())

        temp.pop()

        while temp:
            v = temp.pop()
            self.stack.append(v)
            self.max_stack.append(max(v, self.max_stack[-1]))

        return val


if __name__ == "__main__":
    obj = MaxStack()
    obj.push(5)
    print(obj.stack, obj.max_stack)
    obj.push(1)
    print(obj.stack, obj.max_stack)
    obj.push(5)
    print(obj.stack, obj.max_stack)
    print(obj.top())  # 5
    print(obj.stack, obj.max_stack)
    print(obj.popMax())  # 5
    print(obj.stack, obj.max_stack)
    print(obj.top())  # 1
    print(obj.stack, obj.max_stack)
    print(obj.peekMax())  # 5
    print(obj.stack, obj.max_stack)
    print(obj.pop())  # 1
    print(obj.stack, obj.max_stack)
    print(obj.top())  # 5
    print(obj.stack, obj.max_stack)
