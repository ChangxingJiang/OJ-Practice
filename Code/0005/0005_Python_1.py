class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            m = i - 1
            n = i
            while m >= 0 and n < len(s) and s[m] == s[n]:
                m -= 1
                n += 1
            if n - m - 1 > len(ans):
                ans = s[m + 1:n]
            m = i
            n = i
            while m >= 0 and n < len(s) and s[m] == s[n]:
                m -= 1
                n += 1
            if n - m - 1 > len(ans):
                ans = s[m + 1:n]
        return ans


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))  # "bab"
    print(Solution().longestPalindrome("cbbd"))  # "bb"
    print(Solution().longestPalindrome("a"))  # "a"
