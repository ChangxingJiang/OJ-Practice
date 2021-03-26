import collections


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 统计每个字母的数量
        count = collections.Counter(s)

        # 递归处理字母数量不为偶数的情况
        for ch in ["a", "e", "i", "o", "u"]:
            if count[ch] % 2 == 1:
                idx1 = s.index(ch)
                idx2 = s.rindex(ch)
                return max(self.findTheLongestSubstring(s[:idx2]), self.findTheLongestSubstring(s[idx1 + 1:]))

        # 若均为偶数则返回当前字符串长度
        return len(s)


if __name__ == "__main__":
    print(Solution().findTheLongestSubstring(s="eleetminicoworoep"))  # 13
    print(Solution().findTheLongestSubstring(s="leetcodeisgreat"))  # 5
    print(Solution().findTheLongestSubstring(s="bcbcbc"))  # 6
