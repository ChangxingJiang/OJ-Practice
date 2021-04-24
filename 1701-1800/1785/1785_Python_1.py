import math
from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        diff = abs(sum(nums) - goal)

        if diff == 0:
            return 0
        else:
            return math.ceil(diff / limit)


if __name__ == "__main__":
    print(Solution().minElements(nums=[1, -1, 1], limit=3, goal=-4))  # 2
    print(Solution().minElements(nums=[1, -10, 9, 1], limit=100, goal=0))  # 1
