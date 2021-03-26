class Solution:
    def waysToChange(self, n: int) -> int:
        # 处理1分硬币
        dp = [[1] * (n + 1)] + [[0] * (n + 1) for _ in range(3)]

        # 处理5分硬币
        for i in range(n + 1):
            dp[1][i] = dp[0][i] + (dp[1][i - 5] if i >= 5 else 0)

        # 处理10分硬币
        for i in range(n + 1):
            dp[2][i] = dp[1][i] + (dp[2][i - 10] if i >= 10 else 0)

        # 处理25分硬币
        for i in range(n + 1):
            dp[3][i] = dp[2][i] + (dp[3][i - 25] if i >= 25 else 0)

        return dp[-1][-1] % 1000000007


if __name__ == "__main__":
    print(Solution().waysToChange(5))  # 2
    print(Solution().waysToChange(10))  # 4
    print(Solution().waysToChange(900750))  # 504188296
