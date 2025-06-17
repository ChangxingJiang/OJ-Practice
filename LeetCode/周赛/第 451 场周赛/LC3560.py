class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        # 令 n >= m
        if n < m:
            n, m = m, n

        if m <= k:
            # 不切割
            if n <= k:
                return 0

            # 只切割一刀：尽可能切得差异更大
            elif n <= 2 * k:
                return (n - k) * k

            # 切割两刀：
            else:
                return (n - 2 * k) * (2 * k) + k * k

        else:
            # 各切一刀
            return (n - k) * k + (m - k) * k


if __name__ == "__main__":
    print(Solution().minCuttingCost(n=6, m=5, k=5))  # 5
    print(Solution().minCuttingCost(n=4, m=4, k=6))  # 0

    # 自制用例
    print(Solution().minCuttingCost(n=7, m=1, k=3))  # 15
