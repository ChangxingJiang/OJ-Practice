import functools


class Solution:
    def confusingNumberII(self, N: int) -> int:
        lst = [int(ch) for ch in str(N)]
        size = len(lst)


    @functools.lru_cache(None)
    def b(self, n):
        """n位数以下有多少个旋转之后有效的值（包含0，包含相同的数）"""
        return pow(5, n)

    @functools.lru_cache(None)
    def c(self, n):
        """n位数以下旋转后有多少个数的值不变"""
        if n == 0:
            return 0
        if n == 1:
            return 3
        else:
            return self.b(n) - self.a(n) - self.a(n - 1)

    @functools.lru_cache(None)
    def a(self, n):
        """b位数以下旋转后多少个数不变"""
        if n == 1:
            return 2
        else:
            return self.a(n - 1) + 4 * (self.b(n - 1) - self.c(n - 2))


if __name__ == "__main__":
    print(Solution().confusingNumberII(10))  # 3
    print(Solution().confusingNumberII(20))  # 6
    print(Solution().confusingNumberII(100))  # 19

    print(Solution().confusingNumberII(174))  # 31
