class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0

        dp = [0.0] * (K + W)
        for i in range(K, min(N + 1, K + W)):
            dp[i] = 1

        dp[K - 1] = min(N - K + 1, W) / W

        for i in range(K - 2, -1, -1):
            dp[i] += dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]


if __name__ == "__main__":
    print(Solution().new21Game(10, 1, 10))  # 1.00000
    print(Solution().new21Game(6, 1, 10))  # 0.60000
    print(Solution().new21Game(21, 17, 10))  # 0.73278
    print(Solution().new21Game(9811, 8776, 1096))  # 0.73278
