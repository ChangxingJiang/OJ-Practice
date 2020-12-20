class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        pass


if __name__ == "__main__":
    print(Solution().getHappyString(n=1, k=3))  # "c"
    print(Solution().getHappyString(n=1, k=4))  # ""
    print(Solution().getHappyString(n=3, k=9))  # "cab"
    print(Solution().getHappyString(n=2, k=7))  # ""
    print(Solution().getHappyString(n=10, k=100))  # "abacbabacb"
