class Solution:
    def lastSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            ans = max(ans, s[i:])
        return ans


if __name__ == "__main__":
    print(Solution().lastSubstring("abab"))  # "bab"
    print(Solution().lastSubstring("leetcode"))  # "tcode"
