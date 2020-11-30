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


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        min_val, max_val = min(nums), max(nums)
        B = BIT(max_val - min_val + 1)

        ans = []
        for n in reversed(nums):
            ans.append(B.query(n - min_val))
            B.add(n - min_val + 1, 1)

        ans.reverse()

        return ans


if __name__ == "__main__":
    print(Solution().countSmaller([5, 2, 6, 1]))  # [2,1,1,0]
    print(Solution().countSmaller([]))  # []
    print(Solution().countSmaller([-1]))  # [0]
    print(Solution().countSmaller([-1, -1]))  # [0,0]
