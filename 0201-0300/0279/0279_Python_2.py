class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(v):
            t = int(pow(v, 0.5))
            return t * t == v

        while n % 4 == 0:
            n //= 4

        # 三平方定理
        if n % 8 == 7:
            return 4

        # 直接为完全平方数
        if is_square(n):
            return 1

        # 判断是否如果可以由两个平方数组成
        for i in range(1, int(pow(n, 0.5)) + 1):
            if is_square(n - i * i):
                return 2

        return 3


if __name__ == "__main__":
    print(Solution().numSquares(12))  # 3
    print(Solution().numSquares(13))  # 2
    print(Solution().numSquares(329))  # 3
    print(Solution().numSquares(28))  # 4
