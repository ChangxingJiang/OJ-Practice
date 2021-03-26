from typing import List


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().canDistribute(nums=[1, 2, 3, 4], quantity=[2]))  # False
    print(Solution().canDistribute(nums=[1, 2, 3, 3], quantity=[2]))  # True
    print(Solution().canDistribute(nums=[1, 1, 2, 2], quantity=[2, 2]))  # True
    print(Solution().canDistribute(nums=[1, 1, 2, 3], quantity=[2, 2]))  # False
    print(Solution().canDistribute(nums=[1, 1, 1, 1, 1], quantity=[2, 3]))  # True
