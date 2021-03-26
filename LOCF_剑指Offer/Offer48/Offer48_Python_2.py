class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        last_position = {}
        left = -1
        for right, ch in enumerate(s):
            if ch in last_position and last_position[ch] > left:
                ans = max(ans, right - left-1)
                left = last_position[ch]
                last_position[ch] = right
            else:
                last_position[ch] = right
        ans = max(ans, len(s) - left - 1)

        return ans


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
    print(Solution().lengthOfLongestSubstring("bbbbb"))  # 1
    print(Solution().lengthOfLongestSubstring("pwwkew"))  # 3
    print(Solution().lengthOfLongestSubstring(" "))  # 1
    print(Solution().lengthOfLongestSubstring("au"))  # 2
