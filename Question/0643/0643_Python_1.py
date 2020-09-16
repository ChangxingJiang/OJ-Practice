from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = float("-inf")
        for i in range(len(nums) - k + 1):
            n = sum(nums[i:i + k])
            maximum = max(maximum, n)
        return maximum / k


if __name__ == "__main__":
    print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], k=4))  # 12.75
    print(Solution().findMaxAverage([-1], k=1))  # -1
