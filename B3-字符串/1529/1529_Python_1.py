class Solution:
    def minFlips(self, target: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minFlips(target="10111"))  # 3
    print(Solution().minFlips(target="101"))  # 3
    print(Solution().minFlips(target="00000"))  # 0
    print(Solution().minFlips(target="001011101"))  # 5
