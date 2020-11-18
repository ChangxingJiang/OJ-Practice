from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        N1 = len(grid)
        N2 = len(grid[0])

        dp = [[0] * N2 for _ in range(N1)]
        dp[0][0] = grid[0][0]

        for i in range(1, N1):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, N2):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, N1):
            for j in range(1, N2):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]


if __name__ == "__main__":
    # 12
    print(Solution().maxValue([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
