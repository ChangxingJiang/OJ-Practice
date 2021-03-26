class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min_val is None or x < self.min_val:
            self.min_val = x

    def pop(self) -> None:
        ans = self.stack.pop()
        if ans == self.min_val:
            if self.stack:
                self.min_val = min(self.stack)
            else:
                self.min_val = None

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_val


if __name__ == "__main__":
    pass
