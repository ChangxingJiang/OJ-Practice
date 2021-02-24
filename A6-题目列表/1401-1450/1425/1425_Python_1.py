from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().constrainedSubsetSum(nums=[10, 2, -10, 5, 20], k=2))  # 37
    print(Solution().constrainedSubsetSum(nums=[-1, -2, -3], k=1))  # -1
    print(Solution().constrainedSubsetSum(nums=[10, -2, -10, -5, 20], k=2))  # 23
