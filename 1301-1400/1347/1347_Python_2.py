import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # 统计s和t中的字符数量
        count1 = collections.Counter(s)
        count2 = collections.Counter(t)

        # 统计s与t中字符差异数量
        ans = 0
        for i in range(97, 124):
            ans += abs(count1[chr(i)] - count2[chr(i)])

        return ans // 2


if __name__ == "__main__":
    print(Solution().minSteps(s="bab", t="aba"))  # 1
    print(Solution().minSteps(s="leetcode", t="practice"))  # 5
    print(Solution().minSteps(s="anagram", t="mangaar"))  # 0
    print(Solution().minSteps(s="xxyyzz", t="xxyyzz"))  # 0
    print(Solution().minSteps(s="friend", t="family"))  # 4
