class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = []
        for length in range(minSize, maxSize + 1):
            lst = [0] * 26
            now = 0
            for i in range(len(s)):
                if i < length:
                    idx = ord(s[i]) - 97
                    if lst[idx] == 0:
                        now += 1
                    lst[idx] += 1
                else:
                    idx = ord(s[i]) - 97
                    if lst[idx] == 0:
                        now += 1
                    lst[idx] += 1
                    idx = ord(s[i - length]) - 97
                    lst[idx] -= 1
                    if lst[idx] == 0:
                        now -= 1
                if now <= maxLetters and i >= length - 1:
                    res.append(s[i - length + 1:i + 1])

        ans = 0
        for elem in set(res):
            ans = max(ans, res.count(elem))
        return ans


if __name__ == "__main__":
    print(Solution().maxFreq(s="aababcaab", maxLetters=2, minSize=3, maxSize=4))  # 2
    print(Solution().maxFreq(s="aaaa", maxLetters=1, minSize=3, maxSize=3))  # 2
    print(Solution().maxFreq(s="aabcabcab", maxLetters=2, minSize=2, maxSize=3))  # 3
    print(Solution().maxFreq(s="abcde", maxLetters=2, minSize=3, maxSize=3))  # 0
