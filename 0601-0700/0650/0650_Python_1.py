class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[1] = 0
        for i in range(1, n + 1):
            for j in range(1, n // i):
                dp[i * (j + 1)] = min(dp[i * (j + 1)], dp[i] + 1 + j)
        return dp[-1]


if __name__ == "__main__":
    print(Solution().minSteps(3))  # 3
    print(Solution().minSteps(1))  # 0
