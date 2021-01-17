from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp1 = [0] * 2001
        dp1[1000] = 1
        for k in range(len(nums)):
            dp2 = [0] * 2001
            for i in range(-1000, 1001):
                if dp1[i] > 0:
                    dp2[i + nums[k]] += dp1[i]
                    dp2[i - nums[k]] += dp1[i]
            dp1 = dp2

        return dp1[S + 1000] if S <= 1000 else 0


if __name__ == "__main__":
    print(Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], S=3))  # 5
