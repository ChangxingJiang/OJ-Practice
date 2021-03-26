from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        size = len(nums)

        dp = [0, 0]  # nums[0]<nums[1] ; nums[0]>nums[1]

        for i in range(size):
            # 只调整需要每个最小值的情况即可
            if i % 2 == 0:
                dp[0] += max(nums[i] - nums[i - 1] + 1 if i > 0 and nums[i] >= nums[i - 1] else 0,
                             nums[i] - nums[i + 1] + 1 if i < size - 1 and nums[i] >= nums[i + 1] else 0)
            else:
                dp[1] += max(nums[i] - nums[i - 1] + 1 if nums[i] >= nums[i - 1] else 0,
                             nums[i] - nums[i + 1] + 1 if i < size - 1 and nums[i] >= nums[i + 1] else 0)

        return min(dp[0], dp[1])


if __name__ == "__main__":
    print(Solution().movesToMakeZigzag(nums=[1, 2, 3]))  # 2
    print(Solution().movesToMakeZigzag(nums=[9, 6, 1, 6, 2]))  # 4
    print(Solution().movesToMakeZigzag(nums=[2, 7, 10, 9, 8, 9]))  # 4
