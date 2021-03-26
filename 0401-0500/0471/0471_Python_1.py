class Solution:
    def encode(self, s: str) -> str:
        size = len(s)

        dp = [[""] * size for _ in range(size)]

        for l in range(1, size + 1):
            for i in range(size - l + 1):
                j = i + l - 1
                dp[i][j] = s[i:j + 1]
                if l > 4:
                    # 寻找是否为某一段的重复
                    idx = (s[i:j + 1] + s[i:j + 1]).index(s[i:j + 1], 1)
                    if idx < l:
                        dp[i][j] = str(l // idx) + "[" + dp[i][i + idx - 1] + "]"

                    # 寻找是否有更优解
                    for k in range(i, j):
                        if len(dp[i][k]) + len(dp[k + 1][j]) < len(dp[i][j]):
                            dp[i][j] = dp[i][k] + dp[k + 1][j]

        return dp[0][-1]


if __name__ == "__main__":
    print(Solution().encode(s="aaa"))  # "aaa"
    print(Solution().encode(s="aaaaa"))  # "5[a]"
    print(Solution().encode(s="aaaaaaaaaa"))  # "10[a]"
    print(Solution().encode(s="aabcaabcd"))  # "2[aabc]d"
    print(Solution().encode(s="abbbabbbcabbbabbbc"))  # "2[2[abbb]c]"
