class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[float("inf")] * n for _ in range(n)]

        for i in range(n):
            for j in range(n - i):
                print("i:", i, "j:", j)
                if i == 0:
                    dp[j][j + i] = 0
                elif i == 1:
                    dp[j][j + i] = j + 1
                elif i == 2:
                    dp[j][j + i] = j + 2
                else:
                    for k in range(i - 1):
                        dp[j][j + i] = min(dp[j][j + i], max(dp[j][j + k], dp[j + k + 2][j + i]) + (j + k + 2))
                        # print("k:", (j + k + 2), "->",
                        #       (j, j + k), "=", dp[j][j + k], ";",
                        #       (j + k + 2, j + i), "=", dp[j + k + 2][j + i],
                        #       "->", dp[j][j + k] + dp[j + k + 2][j + i] + (j + k + 2))
                    # print("i:", i, "j:", j, "->", (j, j + i), "=", dp[j][j + i])

        # for row in dp:
        #     print([str(v).zfill(3) for v in row])

        return int(dp[0][-1])


if __name__ == "__main__":
    print(Solution().getMoneyAmount(10))  # 16
