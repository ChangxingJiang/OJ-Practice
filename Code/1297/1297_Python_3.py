import collections


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = collections.Counter()
        for i in range(len(s) - minSize + 1):
            res[s[i:i + minSize]] += 1
        for elem, num in res.most_common():
            if len(set(elem)) <= maxLetters:
                return num
        return 0


if __name__ == "__main__":
    print(Solution().maxFreq(s="aababcaab", maxLetters=2, minSize=3, maxSize=4))  # 2
    print(Solution().maxFreq(s="aaaa", maxLetters=1, minSize=3, maxSize=3))  # 2
    print(Solution().maxFreq(s="aabcabcab", maxLetters=2, minSize=2, maxSize=3))  # 3
    print(Solution().maxFreq(s="abcde", maxLetters=2, minSize=3, maxSize=3))  # 0
