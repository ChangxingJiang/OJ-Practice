class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        while k * 2 <= len(s):
            ans += s[0:k][::-1]
            ans += s[k:k * 2]
            s = s[k * 2:]
        else:
            if k <= len(s):
                ans += s[0:k][::-1]
                ans += s[k:]
            else:
                ans += s[::-1]
        return ans


if __name__ == "__main__":
    print(Solution().reverseStr("abcdefg", 2))  # bacdfeg
