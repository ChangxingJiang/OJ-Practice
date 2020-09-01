class Solution:
    def lastSubstring(self, s: str) -> str:
        ans = s
        for i in range(1, len(s)):
            if s[i] != s[i-1]:  # 如果子串的开头和前一个字符相等的话，一定不会是解
                for j in range(len(s) - i):
                    if ans[j] < s[i + j]:
                        ans = s[i:]
                        break
                    elif ans[j] > s[i + j]:
                        break
        return ans


if __name__ == "__main__":
    print(Solution().lastSubstring("abab"))  # "bab"
    print(Solution().lastSubstring("leetcode"))  # "tcode"
