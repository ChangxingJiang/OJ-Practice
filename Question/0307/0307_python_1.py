from typing import List


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


class NumArray:

    def __init__(self, nums: List[int]):
        self.BIT = BIT(len(nums))
        for i, n in enumerate(nums):
            self.BIT.update(i + 1, n)

    def update(self, i: int, val: int) -> None:
        self.BIT.update(i + 1, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.BIT.range_query(i + 1, j + 1)


if __name__ == "__main__":
    obj = NumArray([1, 3, 5])
    print(obj.sumRange(0, 2))  # 9
    obj.update(1, 2)
    print(obj.sumRange(0, 2))  # 8
