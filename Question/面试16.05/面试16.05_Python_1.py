class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0

        now = 5
        while n >= now:
            ans += n // now
            now *= 5

        return ans


if __name__ == "__main__":
    print(Solution().trailingZeroes(3))  # 0
    print(Solution().trailingZeroes(5))  # 1
    print(Solution().trailingZeroes(30))  # 7
