class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().buddyStrings("ab", "ba"))  # True
    print(Solution().buddyStrings("ab", "ab"))  # False
    print(Solution().buddyStrings("aa", "aa"))  # True
    print(Solution().buddyStrings("aaaaaaabc", "aaaaaaacb"))  # True
    print(Solution().buddyStrings("", "aa"))  # False
