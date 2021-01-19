class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1, s2 = len(text1), len(text2)

        dp = [[0] * (s2 + 1) for _ in range(s1 + 1)]

        for i in range(1, s1 + 1):
            for j in range(1, s2 + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

        return dp[-1][-1]


if __name__ == "__main__":
    print(Solution().longestCommonSubsequence(text1="abcde", text2="ace"))  # 3
    print(Solution().longestCommonSubsequence(text1="abc", text2="abc"))  # 3
    print(Solution().longestCommonSubsequence(text1="abc", text2="def"))  # 0
