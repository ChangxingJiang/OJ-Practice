class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isMatch(s="aa", p="a"))  # False
    print(Solution().isMatch(s="aa", p="*"))  # True
    print(Solution().isMatch(s="cb", p="?a"))  # False
    print(Solution().isMatch(s="adceb", p="*a*b"))  # True
    print(Solution().isMatch(s="acdcb", p="a*c?b"))  # False
