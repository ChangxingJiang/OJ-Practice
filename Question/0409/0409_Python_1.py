import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s)
        has_odd = 0
        ans = 0
        for key, value in count.items():
            ans += (value // 2) * 2
            if has_odd == 0 and value % 2 != 0:
                has_odd = 1
        return ans + has_odd


if __name__ == "__main__":
    print(Solution().longestPalindrome("abccccdd"))  # 7
