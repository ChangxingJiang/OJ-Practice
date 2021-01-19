import functools


class Solution:
    def soupServings(self, N: int) -> float:
        @functools.lru_cache(None)
        def dfs(n, m):
            if n <= 0 and m <= 0:
                return 0.5
            elif n <= 0:
                return 1
            elif m <= 0:
                return 0
            else:
                return 0.25 * (dfs(n - 100, m - 0) + dfs(n - 75, m - 25) + dfs(n - 50, m - 50) + dfs(n - 25, m - 75))

        if N >= 5000:
            return 1  # 近似处理
        else:
            return dfs(N, N)


if __name__ == "__main__":
    print(Solution().soupServings(50))  # 0.625
    print(Solution().soupServings(500))  # 0.916344165802002
    print(Solution().soupServings(5000))  # 0.9999967386599964
