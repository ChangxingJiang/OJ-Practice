import collections


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = collections.Counter()
        lst = [0] * 26
        now = 0
        for i in range(len(s)):
            if i < minSize:
                idx = ord(s[i]) - 97
                if lst[idx] == 0:
                    now += 1
                lst[idx] += 1
            else:
                idx = ord(s[i]) - 97
                if lst[idx] == 0:
                    now += 1
                lst[idx] += 1
                idx = ord(s[i - minSize]) - 97
                lst[idx] -= 1
                if lst[idx] == 0:
                    now -= 1
            if now <= maxLetters and i >= minSize - 1:
                res[s[i - minSize + 1:i + 1]] += 1

        return res.most_common(1)[0][1] if res else 0


if __name__ == "__main__":
    print(Solution().maxFreq(s="aababcaab", maxLetters=2, minSize=3, maxSize=4))  # 2
    print(Solution().maxFreq(s="aaaa", maxLetters=1, minSize=3, maxSize=3))  # 2
    print(Solution().maxFreq(s="aabcabcab", maxLetters=2, minSize=2, maxSize=3))  # 3
    print(Solution().maxFreq(s="abcde", maxLetters=2, minSize=3, maxSize=3))  # 0
