class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 1
        while n >= ans:
            n -= ans
            ans += 1
        return ans - 1


if __name__ == "__main__":
    print(Solution().arrangeCoins(5))  # 2
    print(Solution().arrangeCoins(8))  # 3
