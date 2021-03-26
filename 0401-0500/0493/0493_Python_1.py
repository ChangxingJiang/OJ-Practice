import bisect
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
    def reversePairs(self, nums: List[int]) -> int:
        sorted_nums = list(sorted(nums))
        bit = BIT(len(nums))

        ans = 0

        for num in reversed(nums):
            idx1 = bisect.bisect(sorted_nums, num)
            # print(sorted_nums, num, "->", idx1)
            if idx1 == 0:
                idx1 += 1
            ans += bit.query(idx1)

            # print(num, ":", idx1, bit.query(idx1), "->", ans)

            idx2 = bisect.bisect(sorted_nums, num * 2 + 1)
            # print(sorted_nums, num * 2 + 1, "->", idx2)
            if idx2 == 0:
                idx2 += 1
            if sorted_nums[idx2 - 1] < num * 2 + 1:
                idx2 += 1
            if idx2 <= len(nums):
                bit.add(idx2, 1)

        return ans


if __name__ == "__main__":
    # 2
    print(Solution().reversePairs([1, 3, 2, 3, 1]))

    # 3
    print(Solution().reversePairs([2, 4, 3, 5, 1]))

    # 1
    print(Solution().reversePairs([-5, -5]))

    # 40
    print(Solution().reversePairs(
        [233, 2000000001, 234, 2000000006, 235, 2000000003, 236, 2000000007, 237, 2000000002, 2000000005, 233, 233, 233,
         233, 233, 2000000004]))
