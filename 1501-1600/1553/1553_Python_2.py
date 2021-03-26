import functools


# O(log^2N


class Solution:
    @functools.lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 1:
            return 1
        return min(n % 2 + 1 + self.minDays(n // 2), n % 3 + 1 + self.minDays(n // 3))


if __name__ == "__main__":
    print(Solution().minDays(10))  # 4
    print(Solution().minDays(6))  # 3
    print(Solution().minDays(1))  # 1
    print(Solution().minDays(56))  # 6
    print(Solution().minDays(5))  # 4
    print(Solution().minDays(84806671))  # 32
