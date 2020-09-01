class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        start = 0
        for i in range(len(s)):
            t = s[i - length - 1:i + 1]
            if i - length - 1 >= 0 and t == t[::-1]:
                start = i - length - 1
                length += 2
                continue
            t = s[i - length:i + 1]
            if i - length >= 0 and t == t[::-1]:
                start = i - length
                length += 1
        return s[start:start + length]


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))  # "bab"
    print(Solution().longestPalindrome("cbbd"))  # "bb"
    print(Solution().longestPalindrome("bb"))  # "bb"
    print(Solution().longestPalindrome("a"))  # "a"
