class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        N = len(s)

        dp = [[N] * (k + 1) for _ in range(N + 1)]  # 状态表格：在前i个字符中删除k个字符的最小压缩串长度
        dp[0][0] = 0
        dp[1][0] = 1

        # 完成不删除字符的状态转移
        now = 1
        for i in range(2, N + 1):
            if s[i - 1] == s[i - 2]:
                now += 1
                dp[i][0] = dp[i - 1][0] + (1 if now == 2 or now == 10 or now == 100 else 0)
            else:
                now = 1
                dp[i][0] = dp[i - 1][0] + 1

        # 状态转移
        for i in range(1, N + 1):
            for j in range(1, min(k, i) + 1):
                dp[i][j] = dp[i - 1][j - 1]  # 当直接删除最后一个字符时
                same, diff = 0, 0
                for m in range(i, 0, -1):
                    if s[m - 1] == s[i - 1]:
                        same += 1
                        length = 1 if same == 1 else (2 if same < 10 else (3 if same < 100 else 4))
                        dp[i][j] = min(dp[i][j], dp[m - 1][j - diff] + length)  # 转移到对应位置所需删除的数量为diff，相同值的数量为same
                    else:
                        diff += 1
                        if diff > j:
                            break

        return dp[-1][-1]


if __name__ == "__main__":
    print(Solution().getLengthOfOptimalCompression(s="aaabcccd", k=2))  # 4
    print(Solution().getLengthOfOptimalCompression(s="aabbaa", k=2))  # 2
    print(Solution().getLengthOfOptimalCompression(s="aaaaaaaaaaa", k=0))  # 3
    print(Solution().getLengthOfOptimalCompression(s="bababbaba", k=1))  # 7
