from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = now = sum(nums[0:k])
        for i in range(0, len(nums) - k):
            now = now - nums[i] + nums[i + k]
            maximum = max(maximum, now)
        return maximum / k


if __name__ == "__main__":
    print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], k=4))  # 12.75
    print(Solution().findMaxAverage([-1], k=1))  # -1
