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
    def createSortedArray(self, instructions: List[int]) -> int:
        sorted_instructions = list(sorted(instructions))
        bit = BIT(len(instructions))

        ans = 0

        now = 0
        for num in instructions:
            idx1 = bisect.bisect_left(sorted_instructions, num)
            idx2 = bisect.bisect_right(sorted_instructions, num)
            if idx1 == 0:
                idx1 += 1
            if idx2 == 0:
                idx2 += 1

            val1 = bit.query(idx1)
            val2 = bit.query(idx2)

            # print(sorted_instructions, num, "->", (idx1, idx2), "->", (val1, now - val2), "->", ans)

            ans += min(val1, now - val2)

            bit.add(idx2, 1)

            now += 1

        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    # 1
    print(Solution().createSortedArray(instructions=[1, 5, 6, 2]))

    # 3
    print(Solution().createSortedArray(instructions=[1, 2, 3, 6, 5, 4]))

    # 4
    print(Solution().createSortedArray(instructions=[1, 3, 3, 3, 2, 4, 2, 1, 2]))

    # 43
    print(Solution().createSortedArray(
        instructions=[4, 14, 10, 2, 5, 3, 8, 19, 7, 20, 12, 1, 9, 15, 13, 11, 18, 6, 16, 17]))
