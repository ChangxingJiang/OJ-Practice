class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.stacks = []

    def push(self, val: int) -> None:
        if self.cap > 0:
            if self.stacks and len(self.stacks[-1]) < self.cap:
                self.stacks[-1].append(val)
            else:
                self.stacks.append([val])

    def pop(self) -> int:
        if not self.stacks:
            return -1

        val = self.stacks[-1].pop()

        if not self.stacks[-1]:
            self.stacks.pop()

        return val

    def popAt(self, index: int) -> int:
        if index >= len(self.stacks):
            return -1

        val = self.stacks[index].pop()

        if not self.stacks[index]:
            self.stacks.pop(index)

        return val


if __name__ == "__main__":
    m = StackOfPlates(1)
    m.push(1)
    m.push(2)
    print(m.popAt(1))  # 2
    print(m.pop())  # 1
    print(m.pop())  # -1

    m = StackOfPlates(2)
    m.push(1)
    m.push(2)
    m.push(3)
    print(m.popAt(0))  # 2
    print(m.popAt(0))  # 1
    print(m.popAt(0))  # 3
