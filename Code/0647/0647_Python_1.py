class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)

        ans = 0

        # 处理奇数长度的回文串
        for i in range(N):
            ans += 1
            left, right = i - 1, i + 1
            while 0 <= left and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        # 处理偶数长度的回文串
        for i in range(N - 1):
            left, right = i, i + 1
            while 0 <= left and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        return ans


if __name__ == "__main__":
    print(Solution().countSubstrings("abc"))  # 3
    print(Solution().countSubstrings("aaa"))  # 6
