import functools


class Solution:
    def __init__(self):
        self.total_poured = 0

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        self.total_poured = poured

        if query_row == 0 and query_glass == 0:
            return 1 if poured >= 1 else poured

        poured = 0
        if query_glass - 1 >= 0:
            poured += self.overflow(query_row - 1, query_glass - 1) / 2
        if query_glass <= query_row - 1:
            poured += self.overflow(query_row - 1, query_glass) / 2
        return poured if poured <= 1 else 1

    @functools.lru_cache(None)
    def overflow(self, query_row: int, query_glass: int):
        """计算能够溢出的总量"""
        # 最顶层的情况
        if query_row == 0 and query_glass == 0:
            return self.total_poured - 1 if self.total_poured > 1 else 0

        # 非最顶层的情况
        poured = 0
        if query_glass - 1 >= 0:
            poured += self.overflow(query_row - 1, query_glass - 1) / 2
        if query_glass <= query_row - 1:
            poured += self.overflow(query_row - 1, query_glass) / 2
        return poured - 1 if poured > 1 else 0


if __name__ == "__main__":
    print(Solution().champagneTower(1, 1, 1))  # 0
    print(Solution().champagneTower(2, 1, 1))  # 0.5
    print(Solution().champagneTower(100000009, 33, 17))  # 13583347.932617264
    print(Solution().champagneTower(25, 6, 1))  # 0.1875
    print(Solution().champagneTower(1, 0, 0))  # 1
