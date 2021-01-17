from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not -1000 <= S <= 1000:
            return 0

        dp1 = [0] * 2001
        dp1[1000] = 1
        set1 = {1000}
        for k in range(len(nums)):
            dp2 = [0] * 2001
            set2 = set()
            for i in set1:
                if dp1[i] > 0:
                    dp2[i + nums[k]] += dp1[i]
                    dp2[i - nums[k]] += dp1[i]
                    set2.add(i + nums[k])
                    set2.add(i - nums[k])
            dp1 = dp2
            set1 = set2

        return dp1[S + 1000]


if __name__ == "__main__":
    print(Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], S=3))  # 5
