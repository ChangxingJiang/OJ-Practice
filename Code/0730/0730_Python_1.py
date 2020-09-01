class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        MOD = 10 ** 9 + 7
        N = len(S)

        dp = [[[0] * N for _ in range(N)] for _ in range(4)]  # 状态表格

        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                for k in range(4):
                    ch = ["a", "b", "c", "d"][k]
                    if i == j:
                        if S[i] == ch:
                            # 转移方程：DP[x][i][j] = 1（i=j且S[i]=ch）->即只有一个字符的字符串，包含本身一个以目标字符开头的回文串
                            dp[k][i][j] = 1
                        # 转移方程：DP[x][i][j] = 0（i=j且S[i]!=ch）->即只有一个字符的字符串，没有以目标字符开头的回文串（因默认为0不再设置）
                    else:  # 此时：i<j
                        if S[i] != ch:
                            # 转移方程：DP[x][i][j] = DP[k][i+1][j]（i<j且S[i]!=ch）->因为不是以目标字符开头的，所以以目标字符开头的回文串数量与跳过开头字符的情况相同
                            dp[k][i][j] = dp[k][i + 1][j]
                        elif S[j] != ch:
                            # 转移方程：DP[x][i][j] = DP[k][i+1][j]（i<j且S[j]!=ch）->因为新增字符不是目标字符，所以以目标字符开头的回文串数量与跳过最后一个字符的情况相同
                            dp[k][i][j] = dp[k][i][j - 1]
                        else:  # 此时：i<j且S[i]==S[j]==ch
                            if j == i + 1:
                                # 转移方程：DP[x][i][j] = 2（j=i+1且S[i]=S[j]=ch）->即有两个相同字符的字符串（aa），包含两个非空回文串（a）和（aa）
                                dp[k][i][j] = 2
                            else:  # 此时：i<j+1且S[i]==S[j]==ch
                                # 转移方程：DP[x][i][j] = 2+DP[0][i+1][j-1]+DP[1][i+1][j-1]+DP[2][i+1][j-1]+DP[3][i+1][j-1]
                                # 新增首尾两个字符自行组成的两种情况；以及内部所有回文串增加了嵌套于两个目标字符之间的新回文串
                                dp[k][i][j] = 2  # 通过首尾两个字符（aa）自行组成的回文串（a）和（aa）
                                for m in range(4):  # 累加首尾两个字符内部包含的回文串数量->内部所有的回文串均增加了嵌套于两个目标字符之间的新回文串
                                    dp[k][i][j] += dp[m][i + 1][j - 1]
                                    dp[k][i][j] %= MOD

        ans = 0
        for k in range(4):  # 遍历以每个字符开头的情况
            ans += dp[k][0][N - 1]  # 以目标字符开头的，从头到尾的完整字符串
            ans %= MOD
        return ans


if __name__ == "__main__":
    print(Solution().countPalindromicSubsequences(S="bccb"))  # 6
    print(Solution().countPalindromicSubsequences(S="abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"))  # 104860361
