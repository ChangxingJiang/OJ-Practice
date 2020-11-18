import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        count = collections.Counter()
        last = 0
        for i, ch in enumerate(s):
            count[ch] += 1
            if count[ch] > 1:
                ans = max(ans, i - last)
                while count[ch] > 1 and last < i:
                    count[s[last]] -= 1
                    last += 1
        ans = max(ans, len(s) - last)

        return ans


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
    print(Solution().lengthOfLongestSubstring("bbbbb"))  # 1
    print(Solution().lengthOfLongestSubstring("pwwkew"))  # 3
