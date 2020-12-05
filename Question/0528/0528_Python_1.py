import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.nums = w

        self.prefix = []
        now = 0
        for i, num in enumerate(self.nums):
            now += num
            self.prefix.append(now)

    def pickIndex(self) -> int:
        target = random.randint(0, self.prefix[-1] - 1)
        # print("随机数:", target)

        l, r = 0, len(self.prefix) - 1
        ans = 0
        while l <= r:
            m = (l + r) // 2
            # print(l, r, "->", m, "->", self.prefix[m], target)
            if self.prefix[m] <= target:
                l = m + 1
                ans = m + 1
            else:  # self.prefix[m] > target:
                r = m - 1

        return ans


if __name__ == "__main__":
    obj = Solution([1])
    print(obj.pickIndex())  # 0
    print()

    obj = Solution([1, 3])
    print(obj.pickIndex())  # 1
    print(obj.pickIndex())  # 1
    print(obj.pickIndex())  # 1
    print(obj.pickIndex())  # 1
    print(obj.pickIndex())  # 0
    print()
