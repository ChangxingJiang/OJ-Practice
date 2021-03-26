from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lst = [0] * (max(nums) + 1)
        for num in nums:
            lst[num] += num

        if len(lst) <= 3:
            return max(lst)

        dp = [0] * len(lst)
        dp[1], dp[2] = lst[1], lst[2]
        for i in range(2, len(lst)):
            dp[i] = max(dp[i - 1], dp[i - 2] + lst[i])
        return dp[-1]


if __name__ == "__main__":
    print(Solution().deleteAndEarn(nums=[]))  # 0
    print(Solution().deleteAndEarn(nums=[3, 4, 2]))  # 6
    print(Solution().deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]))  # 9
