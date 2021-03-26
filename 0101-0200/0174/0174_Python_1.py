from typing import List


class Solution:
    _BIG = 2 ** 31

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        # 初始化状态矩阵
        dp = [[self._BIG] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1  # 右下角位置的右侧和下方

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                res = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(res, 1)

        return dp[0][0]


if __name__ == "__main__":
    # 7
    print(Solution().calculateMinimumHP([
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]))

    # 1
    print(Solution().calculateMinimumHP([[0,0]]))
