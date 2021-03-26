# 贪心算法 动态规划 记忆化递归
# O(N×M) M为N开根号


import functools


class Solution:
    # 记忆化递归
    # 超出时间限制

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

    @functools.lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        # 如果n为平方数，Alice获胜
        if n in self.square_set:
            return True

        # 如果不是平方数，判断Alice是否有必胜策略
        return not all([self.winnerSquareGame(n - square) for square in self.square_list if square < n])


if __name__ == "__main__":
    print(Solution().winnerSquareGame(1))  # True
    print(Solution().winnerSquareGame(2))  # False
    print(Solution().winnerSquareGame(3))  # True
    print(Solution().winnerSquareGame(4))  # True
    print(Solution().winnerSquareGame(7))  # False
    print(Solution().winnerSquareGame(17))  # False
    print(Solution().winnerSquareGame(74497))  # False
