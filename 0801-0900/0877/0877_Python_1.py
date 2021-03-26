from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        size = len(piles)

        # dp[n][m]为还剩下n到m颗石子时的状态
        # dp[*][*][0]为先拿的人可以拿到的石子数；dp[*][*][1]为后拿的人可以拿到的石子数
        dp = [[[0, 0] for _ in range(size)] for _ in range(size)]

        # 处理剩余石子为1的情况
        for i in range(size):
            dp[i][i][0] = piles[i]

        # 处理剩余石子不为1的情况
        for l in range(2, size + 1):  # 遍历剩余石子数量
            for i in range(size - l + 1):  # 遍历石子开始位置
                j = i + l - 1  # 计算石子结束位置
                n1 = piles[j] + dp[i][j - 1][1]
                n2 = piles[i] + dp[i + 1][j][1]
                if n1 > n2:
                    dp[i][j][0] = n1
                    dp[i][j][1] = dp[i][j - 1][0]
                else:
                    dp[i][j][0] = n2
                    dp[i][j][1] = dp[i + 1][j][0]

        return dp[0][-1][0] > dp[0][-1][1]


if __name__ == "__main__":
    print(Solution().stoneGame([5, 3, 4, 5]))  # True
