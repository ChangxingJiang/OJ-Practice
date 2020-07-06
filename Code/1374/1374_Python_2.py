class Solution:
    def generateTheString(self, n: int) -> str:
        return "a" * (n - 1) + ("b" if n % 2 == 0 else "a")


if __name__ == "__main__":
    print(Solution().generateTheString(4))  # pppz
    print(Solution().generateTheString(2))  # xy
    print(Solution().generateTheString(7))  # holasss
