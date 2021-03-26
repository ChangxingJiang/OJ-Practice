class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isRationalEqual(S="0.(52)", T="0.5(25)"))  # True
    print(Solution().isRationalEqual(S="0.1666(6)", T="0.166(66)"))  # True
    print(Solution().isRationalEqual(S="0.9(9)", T="1."))  # True
