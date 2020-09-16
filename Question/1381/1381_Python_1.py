class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.stack), k)):
            self.stack[i] += val


if __name__ == "__main__":
    obj = CustomStack(3)
    obj.push(1)
    obj.push(2)
    print(obj.pop())  # 2
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.increment(5, 100)
    obj.increment(2, 100)
    print(obj.pop())  # 103
    print(obj.pop())  # 202
    print(obj.pop())  # 201
    print(obj.pop())  # -1
