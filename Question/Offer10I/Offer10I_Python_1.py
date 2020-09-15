class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b % 1000000007


if __name__ == "__main__":
    print(Solution().fib(2))  # 1
    print(Solution().fib(5))  # 5
