from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.array = deque()
        self.total = 0
        self.size = size

    def next(self, val: int) -> float:
        if len(self.array) == self.size:
            self.total -= self.array.popleft()

        self.array.append(val)
        self.total += val
        return self.total / len(self.array)


if __name__ == "__main__":
    m = MovingAverage(3)
    print(m.next(1))  # 1
    print(m.next(10))  # 11/2
    print(m.next(3))  # 14/3
    print(m.next(5))  # 18/3
