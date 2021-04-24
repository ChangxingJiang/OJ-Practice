from typing import List


class Solution:
    _MAX = 10 ** 6

    def minSideJumps(self, obstacles: List[int]) -> int:
        # 定义状态矩阵
        dp = [self._MAX, 0, self._MAX]

        for num in obstacles:
            if num == 1:
                dp[0] = self._MAX
                dp[1] = min(dp[1], dp[2] + 1)
                dp[2] = min(dp[2], dp[1] + 1)
            elif num == 2:
                dp[1] = self._MAX
                dp[0] = min(dp[0], dp[2] + 1)
                dp[2] = min(dp[2], dp[0] + 1)
            elif num == 3:
                dp[2] = self._MAX
                dp[0] = min(dp[0], dp[1] + 1)
                dp[1] = min(dp[1], dp[0] + 1)
            else:  # num == 0
                dp[0] = min(dp[0], dp[1] + 1, dp[2] + 1)
                dp[1] = min(dp[1], dp[0] + 1, dp[2] + 1)
                dp[2] = min(dp[2], dp[0] + 1, dp[1] + 1)

        return min(dp)


if __name__ == "__main__":
    print(Solution().minSideJumps([0, 1, 2, 3, 0]))  # 2
    print(Solution().minSideJumps([0, 1, 1, 3, 3, 0]))  # 0
    print(Solution().minSideJumps([0, 2, 1, 0, 3, 0]))  # 2
