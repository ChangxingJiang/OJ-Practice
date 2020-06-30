from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = [sum(nums[0:k])] * (len(nums) - k + 1)
        for i in range(0, len(nums) - k):
            maximum[i] = maximum[i - 1] - nums[i] + nums[i + k]
        return max(maximum) / k


if __name__ == "__main__":
    print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], k=4))  # 12.75
    print(Solution().findMaxAverage([-1], k=1))  # -1
