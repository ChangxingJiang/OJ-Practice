class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isMatch("aa", "a"))  # True
    print(Solution().isMatch("aa", "a*"))  # True
    print(Solution().isMatch("ab", ".*"))  # True
    print(Solution().isMatch("aab", "c*a*b"))  # True
    print(Solution().isMatch("mississippi", "mis*is*p*."))  # False
