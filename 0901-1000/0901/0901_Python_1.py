class StockSpanner:
    def __init__(self):
        self.stack = []
        self.idx = 0

    def next(self, price: int) -> int:
        self.idx += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        self.stack.append([price, self.idx])
        if len(self.stack) > 1:
            return self.idx - self.stack[-2][1]
        else:
            return self.idx


if __name__ == "__main__":
    obj = StockSpanner()
    print(obj.next(100))  # 1
    print(obj.next(80))  # 1
    print(obj.next(60))  # 1
    print(obj.next(70))  # 2
    print(obj.next(60))  # 1
    print(obj.next(75))  # 4
    print(obj.next(85))  # 6
