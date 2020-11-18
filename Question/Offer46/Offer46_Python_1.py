class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)

        # 定义状态列表
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, len(s)):
            if s[i - 1] != "0" and int(s[i - 1:i + 1]) < 26:
                dp[i + 1] = dp[i - 1] + dp[i]
            else:
                dp[i + 1] = dp[i]

        return dp[-1]


if __name__ == "__main__":
    print(Solution().translateNum(12258))  # 5
    print(Solution().translateNum(506))  # 1
