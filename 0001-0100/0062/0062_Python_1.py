class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1

        for j in range(m):
            dp[0][j] = 1

        for i in range(n):
            dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    print(Solution().uniquePaths(3, 2))  # 3
    print(Solution().uniquePaths(7, 3))  # 28
