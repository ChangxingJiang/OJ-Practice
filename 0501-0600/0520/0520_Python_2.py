class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower() or word.isupper():
            return True
        return word[0].isupper() and word[1:].islower()


if __name__ == "__main__":
    print(Solution().detectCapitalUse("USA"))  # True
    print(Solution().detectCapitalUse("FlaG"))  # False
    print(Solution().detectCapitalUse("FFFFFFFFFFFFFFFFFFFFf"))  # False
