# 贪心算法 动态规划 记忆化递归
# O(N×M) M为N开根号


class Solution:
    # 动态规划

    def __init__(self):
        # 计算范围内的完全平方数
        # O(logN)
        self.square_list = []
        now = 1
        while True:
            square = now ** 2
            if square <= 10 ** 5:
                self.square_list.append(square)
                now += 1
            else:
                break
        self.square_set = set(self.square_list)

    def winnerSquareGame(self, n: int) -> bool:
        # 定义状态表格
        dp = [False] * n

        for i in range(n):
            num = i + 1

            # 如果n为平方数，先手方获胜
            if num in self.square_set:
                dp[i] = True

            # 如果不是平方数，判断先手方是否有必胜策略
            else:
                dp[i] = not all([dp[num - square - 1] for square in self.square_list if square < num])

        # print(dp)

        return dp[-1]


if __name__ == "__main__":
    print(Solution().winnerSquareGame(1))  # True
    print(Solution().winnerSquareGame(2))  # False
    print(Solution().winnerSquareGame(3))  # True
    print(Solution().winnerSquareGame(4))  # True
    print(Solution().winnerSquareGame(7))  # False
    print(Solution().winnerSquareGame(17))  # False
    print(Solution().winnerSquareGame(47))  # True
    print(Solution().winnerSquareGame(74497))  # False
