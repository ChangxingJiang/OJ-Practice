class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        for i in range(N, 0, -1):
            if s[:i] == s[:i][::-1]:
                return s[i:][::-1] + s[:i] + s[i:]
        return ""


if __name__ == "__main__":
    print(Solution().shortestPalindrome("aacecaaa"))  # "aaacecaaa"
    print(Solution().shortestPalindrome("abcd"))  # "dcbabcd"
    print(Solution().shortestPalindrome(""))  # ""
