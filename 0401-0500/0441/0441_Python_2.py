class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((pow(8 * n + 1, 0.5) - 1) / 2)


if __name__ == "__main__":
    print(Solution().arrangeCoins(5))  # 2
    print(Solution().arrangeCoins(8))  # 3
