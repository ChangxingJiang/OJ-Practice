class Solution:
    def fib(self, N: int) -> int:
        x = (1 + 5 ** 0.5) / 2
        return int((x ** N + 1) / 5 ** 0.5)


if __name__ == "__main__":
    print(Solution().fib(2))  # 1
    print(Solution().fib(3))  # 2
    print(Solution().fib(4))  # 3
