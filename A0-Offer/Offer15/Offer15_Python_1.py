class Solution:
    def hammingWeight(self, n: int) -> int:
        pass


if __name__ == "__main__":
    # 3
    print(Solution().hammingWeight(int("00000000000000000000000000001011", base=2)))

    # 1
    print(Solution().hammingWeight(int("00000000000000000000000010000000", base=2)))

    # 31
    print(Solution().hammingWeight(int("11111111111111111111111111111101", base=2)))
