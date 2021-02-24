class Solution:
    _MOD = 10 ** 9 + 7

    def findDerangement(self, n: int) -> int:
        dp = [0] * max(2, n + 1)
        dp[0], dp[1] = 1, 0
        for i in range(2, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % self._MOD
        return dp[n]


if __name__ == "__main__":
    print(Solution().findDerangement(3))  # 2
