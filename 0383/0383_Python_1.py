class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().canConstruct("a", "b"))  # False
    print(Solution().canConstruct("aa", "ab"))  # False
    print(Solution().canConstruct("aa", "aab"))  # True
