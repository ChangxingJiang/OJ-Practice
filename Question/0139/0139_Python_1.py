import collections
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False

        words = set(wordDict)
        max_length = max(len(word) for word in words)

        window = collections.deque([0])
        for i2 in range(1, len(s) + 1):
            if i2 - window[0] > max_length:
                window.popleft()
            if not window:
                return False
            for i1 in window:
                if s[i1:i2] in words:
                    window.append(i2)
                    break

        return window[-1] == len(s)


if __name__ == "__main__":
    print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))  # True
    print(Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"]))  # True
    print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))  # False
    print(Solution().wordBreak(s="a", wordDict=[]))  # False
    print(Solution().wordBreak(s="ccbb", wordDict=["bc", "cb"]))  # False
