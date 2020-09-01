class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().canConvertString(s="input", t="ouput", k=9))  # True
    print(Solution().canConvertString(s="abc", t="bcd", k=10))  # False
    print(Solution().canConvertString(s="aab", t="bbb", k=27))  # True
