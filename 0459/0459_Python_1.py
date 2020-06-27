class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern("abab"))  # True
    print(Solution().repeatedSubstringPattern("aba"))  # False
    print(Solution().repeatedSubstringPattern("abcabcabcabc"))  # True
