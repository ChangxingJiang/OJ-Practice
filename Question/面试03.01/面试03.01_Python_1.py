class TripleInOne:

    def __init__(self, stackSize: int):
        self.size = stackSize
        self.lst = [-1] * (self.size * 3)
        self.idx = [0, self.size, self.size * 2]  # 头结点
        self.length = [0, 0, 0]  # 当前长度

    def push(self, stackNum: int, value: int) -> None:
        if self.length[stackNum] < self.size:
            self.lst[self.idx[stackNum] + self.length[stackNum]] = value
            self.length[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        if not self.isEmpty(stackNum):
            val = self.lst[self.idx[stackNum] + self.length[stackNum] - 1]
            self.length[stackNum] -= 1
            return val
        else:
            return -1

    def peek(self, stackNum: int) -> int:
        if not self.isEmpty(stackNum):
            return self.lst[self.idx[stackNum] + self.length[stackNum] - 1]
        else:
            return -1

    def isEmpty(self, stackNum: int) -> bool:
        return self.length[stackNum] == 0


if __name__ == "__main__":
    stack = TripleInOne(1)
    stack.push(0, 1)
    stack.push(0, 2)
    print(stack.pop(0))  # 1
    print(stack.pop(0))  # -1
    print(stack.pop(0))  # -1
    print(stack.isEmpty(0))  # True

    stack = TripleInOne(2)
    stack.push(0, 1)
    stack.push(0, 2)
    stack.push(0, 3)
    print(stack.pop(0))  # 2
    print(stack.pop(0))  # 1
    print(stack.pop(0))  # -1
    print(stack.peek(0))  # -1
