class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(i1, i2):
            while i1 < i2:
                if s[i1] != s[i2]:
                    return False
                i1 += 1
                i2 -= 1
            return True

        idx1, idx2 = 0, len(s) - 1
        while idx1 <= idx2:
            if s[idx1] != s[idx2]:
                return helper(idx1 + 1, idx2) or helper(idx1, idx2 - 1)
            idx1 += 1
            idx2 -= 1
        return True


if __name__ == "__main__":
    print(Solution().validPalindrome("aba"))  # True
    print(Solution().validPalindrome("abc"))  # False
    print(Solution().validPalindrome("abca"))  # True
    print(Solution().validPalindrome(
        "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))  # True
