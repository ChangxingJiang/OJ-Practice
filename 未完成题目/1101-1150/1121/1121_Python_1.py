from typing import List


class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        pass


if __name__ == "__main__":
    # True
    print(Solution().canDivideIntoSubsequences(nums=[1, 2, 2, 3, 3, 4, 4], K=3))

    # False
    print(Solution().canDivideIntoSubsequences(nums=[5, 6, 6, 7, 8], K=3))
