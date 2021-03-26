class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        i1, i2, i3 = 0, 0, 0
        for i in range(1, n):
            n1, n2, n3 = dp[i1] * 2, dp[i2] * 3, dp[i3] * 5
            dp[i] = min(n1, n2, n3)
            if n1 == dp[i]:
                i1 += 1
            if n2 == dp[i]:
                i2 += 1
            if n3 == dp[i]:
                i3 += 1
        return dp[-1]


if __name__ == "__main__":
    print(Solution().nthUglyNumber(10))  # 12
