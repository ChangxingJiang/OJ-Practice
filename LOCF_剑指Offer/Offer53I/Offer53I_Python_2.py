import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect.bisect_right(nums, target) - bisect.bisect_left(nums, target)


if __name__ == "__main__":
    print(Solution().search([5, 7, 7, 8, 8, 10], 8))  # 2
    print(Solution().search([5, 7, 7, 8, 8, 10], 6))  # 0
