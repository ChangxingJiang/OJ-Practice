class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, "", 1)
            else:
                return False
        else:
            return True


if __name__ == "__main__":
    print(Solution().canConstruct("a", "b"))  # False
    print(Solution().canConstruct("aa", "ab"))  # False
    print(Solution().canConstruct("aa", "aab"))  # True
