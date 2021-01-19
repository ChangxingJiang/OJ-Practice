from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(m)]  # 左上右下

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i > 0:
                        dp[i][j][0] = dp[i - 1][j][0] + 1
                    else:
                        dp[i][j][0] = 1

                    if j > 0:
                        dp[i][j][1] = dp[i][j - 1][1] + 1
                    else:
                        dp[i][j][1] = 1

        ans = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    if i < m - 1:
                        dp[i][j][2] = dp[i + 1][j][2] + 1
                    else:
                        dp[i][j][2] = 1

                    if j < n - 1:
                        dp[i][j][3] = dp[i][j + 1][3] + 1
                    else:
                        dp[i][j][3] = 1

                    v1 = min(dp[i][j][2], dp[i][j][3])

                    if v1 > ans:
                        for v2 in range(ans + 1, v1 + 1):
                            if v2 > ans:
                                if min(dp[i + v2 - 1][j + v2 - 1][0], dp[i + v2 - 1][j + v2 - 1][1]) >= v2:
                                    ans = v2

        return ans * ans


if __name__ == "__main__":
    # 9
    print(Solution().largest1BorderedSquare(grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))

    # 1
    print(Solution().largest1BorderedSquare(grid=[[1, 1, 0, 0]]))

    # 9
    print(Solution().largest1BorderedSquare(grid=[[0, 1, 1, 1, 1, 1, 1, 0],
                                                  [1, 1, 1, 1, 1, 1, 1, 1],
                                                  [1, 0, 1, 1, 1, 0, 1, 1],
                                                  [1, 1, 1, 1, 0, 1, 1, 1],
                                                  [1, 0, 1, 0, 0, 1, 1, 1],
                                                  [0, 1, 1, 1, 1, 0, 1, 1]]))
