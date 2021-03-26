import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        idx = 0
        ans = 0
        for i, n in enumerate(self.nums):
            if n == target:
                idx += 1
                rand = random.randint(1, idx)
                if rand == idx:
                    ans = i
        return ans


if __name__ == "__main__":
    obj = Solution([1, 2, 3, 3, 3])
    print(obj.pick(3))  # 2 或 3 或 4
    print(obj.pick(1))  # 0
