class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        hashmap = {}  # 距离当前位置最近的字符坐标
        now = 0  # 当前长度
        for i, ch in enumerate(s):
            now += 1
            if ch in hashmap:
                now = min(now, i - hashmap[ch])
            hashmap[ch] = i
            ans = max(ans, now)
        return ans


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
    print(Solution().lengthOfLongestSubstring("bbbbb"))  # 1
    print(Solution().lengthOfLongestSubstring("pwwkew"))  # 3
    print(Solution().lengthOfLongestSubstring(" "))  # 1
    print(Solution().lengthOfLongestSubstring(""))  # 0
    print(Solution().lengthOfLongestSubstring("au"))  # 2
    print(Solution().lengthOfLongestSubstring("ohomm"))  # 3
    print(Solution().lengthOfLongestSubstring("abba"))  # 2
    print(Solution().lengthOfLongestSubstring("tmmzuxt"))  # 5
