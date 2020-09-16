class Solution:
    def integerBreak(self, n: int) -> int:
        ans = 0
        for m in range(2, n + 1):
            a, b = divmod(n, m)
            lst = [a + 1 if i < b else a for i in range(m)]
            val = 1
            for v in lst:
                val *= v
            if val >= ans:
                ans = val
            else:
                break

        return ans


if __name__ == "__main__":
    print(Solution().integerBreak(2))  # 1
    print(Solution().integerBreak(10))  # 36
