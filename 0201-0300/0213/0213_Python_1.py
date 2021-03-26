from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        size = len(nums)

        # 偷第1家的情况
        dp1 = [[0] * 2 for _ in range(size)]  # dp[i][0]=偷了这一家的最大值，dp[i][1]=没偷这一家的最大值
        dp1[0] = [nums[0], 0]
        for i in range(1, size - 1):
            dp1[i][0] = dp1[i - 1][1] + nums[i]
            dp1[i][1] = max(dp1[i - 1][0], dp1[i - 1][1])
        dp1[-1][1] = max(dp1[-2][0], dp1[-2][1])  # 最后1不能偷

        # 没偷第1家的情况
        dp2 = [[0] * 2 for _ in range(size)]
        for i in range(1, size):
            dp2[i][0] = dp2[i - 1][1] + nums[i]
            dp2[i][1] = max(dp2[i - 1][0], dp2[i - 1][1])

        return max(dp1[-1][1], dp2[-1][0], dp2[-1][1])


if __name__ == "__main__":
    print(Solution().rob(nums=[2, 3, 2]))  # 3
    print(Solution().rob(nums=[1, 2, 3, 1]))  # 4
    print(Solution().rob(nums=[0]))  # 0

    # 自制用例
    print(Solution().rob(nums=[3, 1, 1, 4, 2, 5]))  # 10
