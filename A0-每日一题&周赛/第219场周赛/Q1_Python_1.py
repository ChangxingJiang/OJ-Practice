class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1


if __name__ == "__main__":
    print(Solution().numberOfMatches(7))  # 6
    print(Solution().numberOfMatches(14))  # 13
