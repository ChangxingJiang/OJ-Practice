class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1

        x1 = 0
        x2 = 1
        for _ in range(1, N):
            x1, x2 = x2, x1 + x2

        return x2


if __name__ == "__main__":
    print(Solution().fib(2))  # 1
    print(Solution().fib(3))  # 2
    print(Solution().fib(4))  # 3
