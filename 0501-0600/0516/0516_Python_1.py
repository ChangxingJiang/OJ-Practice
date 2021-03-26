class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)

        dp = [[0] * size for _ in range(size)]
        for i in range(size):
            dp[i][i] = 1

        for i in range(size - 1, -1, -1):
            for j in range(i + 1, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]


if __name__ == "__main__":
    print(Solution().longestPalindromeSubseq("bbbab"))  # 4
    print(Solution().longestPalindromeSubseq("cbbd"))  # 2
