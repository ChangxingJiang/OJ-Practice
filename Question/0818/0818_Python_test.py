class Solution(object):
    def racecar(self, target):
        dp = [0, 1, 4] + [float('inf')] * target
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2 ** k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                val = dp[t - 2 ** (k - 1) + 2 ** j] + k - 1 + j + 2
                if val < dp[t]:
                    # print(t, k, "->", t - 2 ** (k - 1) + 2 ** j, k, j)
                    dp[t] = val
                # dp[t] = min(dp[t], val)
            if 2 ** k - 1 - t < t:
                dp[t] = min(dp[t], dp[2 ** k - 1 - t] + k + 1)
        print(dp)
        return dp[target]


if __name__ == "__main__":
    print(Solution().racecar(3))  # 2
    print(Solution().racecar(5))  # 7
    print(Solution().racecar(6))  # 5
    print(Solution().racecar(20))  # 12
    print(Solution().racecar(28))  # 8
