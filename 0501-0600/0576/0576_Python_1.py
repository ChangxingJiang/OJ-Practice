class Solution:
    def findPaths(self, m: int, n: int, t: int, ii: int, jj: int) -> int:
        def _is_valid(x, y):
            return 1 <= x <= m and 1 <= y <= n

        def _get_neighbors(x1, y1):
            return [(x2, y2) for (x2, y2) in [(x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)]
                    if _is_valid(x2, y2)]

        # 初始化状态矩阵
        dp = [[[0] * (n + 2) for _ in range(m + 2)] for _ in range(t + 1)]
        dp[0][ii + 1][jj + 1] = 1

        # 状态转移
        ans = 0
        for k in range(1, t + 1):
            for i1 in range(m + 2):
                for j1 in range(n + 2):
                    for (i2, j2) in _get_neighbors(i1, j1):
                        dp[k][i1][j1] += dp[k - 1][i2][j2]
                    if i1 == 0 or i1 == m + 1 or j1 == 0 or j1 == n + 1:
                        ans += dp[k][i1][j1]
            # print("第{}步".format(k))
            # for row in dp[k]:
            #     print(row)

        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().findPaths(m=2, n=2, t=2, ii=0, jj=0))  # 6
    print(Solution().findPaths(m=1, n=3, t=3, ii=0, jj=1))  # 12
