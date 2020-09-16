from typing import List

import collections

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        pattern = collections.Counter(chars)
        ans = 0
        for word in words:
            for c in word:
                if c not in pattern or word.count(c) > pattern[c]:
                    break
            else:
                ans += len(word)
        return ans


if __name__ == "__main__":
    print(Solution().countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach"))  # 6
    print(Solution().countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr"))  # 10
