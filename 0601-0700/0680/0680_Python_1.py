class Solution:
    def __init__(self):
        self.wrong = 0

    def validPalindrome(self, s: str) -> bool:
        idx1 = 0
        idx2 = len(s) - 1
        while idx1 <= idx2:
            if s[idx1] != s[idx2]:
                self.wrong += 1
                if self.wrong >= 2:
                    return False

                sf1 = s[:idx1] + s[idx1 + 1:]
                sf2 = s[:idx2] + s[idx2 + 1:]
                return self.validPalindrome(sf1) or self.validPalindrome(sf2)
            idx1 += 1
            idx2 -= 1
        return True


if __name__ == "__main__":
    print(Solution().validPalindrome("aba"))  # True
    print(Solution().validPalindrome("abc"))  # False
    print(Solution().validPalindrome("abca"))  # True
    print(Solution().validPalindrome(
        "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))  # True
