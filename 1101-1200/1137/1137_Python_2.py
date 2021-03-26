class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        x1 = 0
        x2 = 1
        x3 = 1
        for i in range(3, n + 1):
            x1, x2, x3 = x2, x3, x1 + x2 + x3
        return x3


if __name__ == "__main__":
    print(Solution().tribonacci(n=0))  # 0
    print(Solution().tribonacci(n=4))  # 4
    print(Solution().tribonacci(n=25))  # 1389537
