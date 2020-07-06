from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().minSubsequence(nums=[4, 3, 10, 9, 8]))  # [10,9]
    print(Solution().minSubsequence(nums=[4, 4, 7, 6, 7]))  # [7,7,6]
    print(Solution().minSubsequence(nums=[6]))  # [6]
