import collections
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 处理特殊情况
        if not s or not words:
            return []

        L = len(words[0])
        total = L * len(words)
        words = collections.Counter(words)
        N = len(s)
        ans = []
        for i in range(L):
            left = i
            right = i
            now = collections.Counter()
            while right < N:
                if right - left < total:
                    now[s[right:right + L]] += 1
                    right += L
                    if right - left == total and now == words:
                        ans.append(left)
                elif right - left == total:
                    now[s[left:left + L]] -= 1
                    if now[s[left:left + L]] == 0:
                        del now[s[left:left + L]]
                    now[s[right:right + L]] += 1
                    left += L
                    right += L
                    if now == words:
                        ans.append(left)
        return ans


if __name__ == "__main__":
    print(Solution().findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))  # [0,9]
    print(Solution().findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))  # []
    print(Solution().findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "good"]))  # [8]
