class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().wordPattern("abba", "dog cat cat dog"))  # True
    print(Solution().wordPattern("abba", "dog cat cat fish"))  # False
    print(Solution().wordPattern("aaaa", "dog cat cat dog"))  # False
    print(Solution().wordPattern("abba", "dog dog dog dog"))  # False
