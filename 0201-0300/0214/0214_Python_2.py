class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        idx1 = 0
        for idx2 in range(N - 1, -1, -1):
            if s[idx1] == s[idx2]:
                idx1 += 1
        if idx1 == N:
            return s
        return s[idx1:][::-1] + self.shortestPalindrome(s[:idx1]) + s[idx1:]


if __name__ == "__main__":
    print(Solution().shortestPalindrome("aacecaaa"))  # "aaacecaaa"
    print(Solution().shortestPalindrome("abcd"))  # "dcbabcd"
    print(Solution().shortestPalindrome(""))  # ""
