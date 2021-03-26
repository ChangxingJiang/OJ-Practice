class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        return ans * n


if __name__ == "__main__":
    print(Solution().integerBreak(2))  # 1
    print(Solution().integerBreak(10))  # 36
