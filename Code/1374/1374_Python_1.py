class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return "a" + "b" * (n - 1)
        else:
            return "a" * n


if __name__ == "__main__":
    print(Solution().generateTheString(4))  # pppz
    print(Solution().generateTheString(2))  # xy
    print(Solution().generateTheString(7))  # holasss
