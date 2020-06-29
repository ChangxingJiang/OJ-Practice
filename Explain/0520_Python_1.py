class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lower_num = 0
        upper_num = 0
        for c in word:
            if ord(c) >= 97:
                if upper_num >= 2:
                    return False
                else:
                    lower_num += 1
            else:
                if lower_num > 0:
                    return False
                else:
                    upper_num += 1
        else:
            return True


if __name__ == "__main__":
    print(Solution().detectCapitalUse("USA"))  # True
    print(Solution().detectCapitalUse("FlaG"))  # False
    print(Solution().detectCapitalUse("FFFFFFFFFFFFFFFFFFFFf"))  # False
