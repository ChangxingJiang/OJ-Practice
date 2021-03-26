import functools


class Solution:
    def __init__(self):
        self.squares = []

    def numSquares(self, n: int) -> int:
        self.squares = [i ** 2 for i in range(1, int(pow(n, 0.5)) + 1)]
        return self.dfs(n, len(self.squares) - 1)

    @functools.lru_cache(None)
    def dfs(self, n, idx):
        # 处理递归完成的情况
        if n == 0:
            return 0
        if idx == 0:
            return n

        # 处理递归未完成的情况
        res = self.dfs(n, idx - 1)
        for i in range(1, n // self.squares[idx] + 1):
            res = min(res, self.dfs(n - i * self.squares[idx], idx - 1) + i)

        return res


if __name__ == "__main__":
    print(Solution().numSquares(12))  # 3
    print(Solution().numSquares(13))  # 2
    print(Solution().numSquares(329))  # 2
