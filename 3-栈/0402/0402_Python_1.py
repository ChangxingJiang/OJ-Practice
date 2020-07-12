class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        pass


if __name__ == "__main__":
    print(Solution().removeKdigits(num="1432219", k=3))  # "1219"
    print(Solution().removeKdigits(num="10200", k=1))  # "200"
    print(Solution().removeKdigits(num="10", k=2))  # "0"
