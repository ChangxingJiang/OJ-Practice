class BIT:
    def __init__(self, n: int):
        self.n = n
        self._tree = [0] * (n + 1)

    @staticmethod
    def _lowbit(x):
        return x & (-x)

    def update(self, i: int, x: int):
        self.add(i, x - (self.query(i) - self.query(i - 1)))

    def add(self, i: int, x: int):
        while i <= self.n:
            self._tree[i] += x
            i += BIT._lowbit(i)

    def query(self, i: int) -> int:
        ans = 0
        while i > 0:
            ans += self._tree[i]
            i -= BIT._lowbit(i)
        return ans

    def range_query(self, l: int, r: int) -> int:
        return self.query(r) - self.query(l - 1)


class StreamRank:

    def __init__(self):
        self.B = BIT(50001)

    def track(self, x: int) -> None:
        self.B.add(x + 1, 1)

    def getRankOfNumber(self, x: int) -> int:
        return self.B.query(x + 1)


if __name__ == "__main__":
    s = StreamRank()
    print(s.getRankOfNumber(1))  # 0
    s.track(0)
    print(s.getRankOfNumber(0))  # 1
