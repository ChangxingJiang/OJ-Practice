class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b, c = 1, 2, 4
        for i in range(3, n):
            a, b, c = b, c, a + b + c
            a %= 1000000007
            b %= 1000000007
            c %= 1000000007
        return c


if __name__ == "__main__":
    print(Solution().waysToStep(1))  # 4
    print(Solution().waysToStep(3))  # 4
    print(Solution().waysToStep(5))  # 13
