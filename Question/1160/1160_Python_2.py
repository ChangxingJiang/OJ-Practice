import collections
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        pattern = collections.Counter(chars)
        ans = 0
        for word in words:
            count = pattern.copy()
            for c in word:
                if c not in count or count[c] <= 0:
                    break
                else:
                    count[c] -= 1
            else:
                ans += len(word)
        return ans


if __name__ == "__main__":
    print(Solution().countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach"))  # 6
    print(Solution().countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr"))  # 10
