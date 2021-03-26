from typing import List


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().largestSubarray(nums=[1, 4, 5, 2, 3], k=3))  # [5,2,3]
    print(Solution().largestSubarray(nums=[1, 4, 5, 2, 3], k=4))  # [4,5,2,3]
    print(Solution().largestSubarray(nums=[1, 4, 5, 2, 3], k=1))  # [5]
