from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxNonOverlapping(nums=[1, 1, 1, 1, 1], target=2))  # 2
    print(Solution().maxNonOverlapping(nums=[-1, 3, 5, 1, 4, 2, -9], target=6))  # 2
    print(Solution().maxNonOverlapping(nums=[-2, 6, 6, 3, 5, 4, 1, 2, 8], target=10))  # 3
    print(Solution().maxNonOverlapping(nums=[0, 0, 0], target=0))  # 3
