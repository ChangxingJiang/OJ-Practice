import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        return [left, right - 1] if left != right else [-1, -1]


if __name__ == "__main__":
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))  # [3,4]
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1,-1]
