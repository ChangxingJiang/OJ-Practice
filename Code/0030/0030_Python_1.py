import collections
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 处理特殊情况
        if not s or not words:
            return []

        L = len(words[0])
        total = len(words[0]) * len(words)
        words = collections.Counter(words)
        N = len(s)
        ans = []
        for i in range(N - total + 1):
            tmp = [s[i + j:i + j + L] for j in range(0, total, L)]
            for key, value in words.items():
                if tmp.count(key) != value:
                    break
            else:
                ans.append(i)
        return ans


if __name__ == "__main__":
    print(Solution().findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))  # [0,9]
    print(Solution().findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))  # []
    print(Solution().findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "good"]))  # [8]
