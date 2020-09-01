import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # 统计t中的字符数量
        count = collections.Counter(t)

        # 统计s与t中字符差异数量
        for ch in s:
            if ch in count:
                count[ch] -= 1

        # 统计s比t多和少的字符数量
        much = 0
        less = 0
        for k, v in count.items():
            if v < 0:
                less -= v
            elif v > 0:
                much += v

        # 返回结果
        return max(much, less)


if __name__ == "__main__":
    print(Solution().minSteps(s="bab", t="aba"))  # 1
    print(Solution().minSteps(s="leetcode", t="practice"))  # 5
    print(Solution().minSteps(s="anagram", t="mangaar"))  # 0
    print(Solution().minSteps(s="xxyyzz", t="xxyyzz"))  # 0
    print(Solution().minSteps(s="friend", t="family"))  # 4
