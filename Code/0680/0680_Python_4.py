class Solution:
    def validPalindrome(self, s: str) -> bool:
        size = len(s)
        r = s[::-1]
        if s == r:
            return True
        for i in range(size):
            if r[i] != s[i]:
                new_s = s[:i] + s[i + 1:]
                new_r = r[:size - i - 1] + r[size - i:]
                if new_s == new_r:
                    return True
                new_s = s[:size - i - 1] + s[size - i:]
                new_r = r[:i] + r[i + 1:]
                if new_s == new_r:
                    return True
                break
        return False


if __name__ == "__main__":
    print(Solution().validPalindrome("aba"))  # True
    print(Solution().validPalindrome("abc"))  # False
    print(Solution().validPalindrome("abca"))  # True
    print(Solution().validPalindrome(
        "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))  # True
