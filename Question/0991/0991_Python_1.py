import functools


class Solution:
    _BIG = 10 ** 9

    @functools.lru_cache(None)
    def brokenCalc(self, x: int, y: int) -> int:
        if x > y:
            return x - y
        if x == y:
            return 0

        if y % 2 == 0:
            return self.brokenCalc(x, y // 2) + 1
        else:
            return self.brokenCalc(x, y + 1) + 1


if __name__ == "__main__":
    print(Solution().brokenCalc(2, 3))  # 2
    print(Solution().brokenCalc(5, 8))  # 2
    print(Solution().brokenCalc(3, 10))  # 3
    print(Solution().brokenCalc(1024, 1))  # 1023
