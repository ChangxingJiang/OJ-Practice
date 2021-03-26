from typing import List


class Solution:
    _BIG = 200 * 100

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = grid[i][j] + min((dp[i - 1][j] if i > 0 else self._BIG),
                                                (dp[i][j - 1] if j > 0 else self._BIG))

        return dp[-1][-1]


if __name__ == "__main__":
    print(Solution().minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # 7
    print(Solution().minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))  # 12
