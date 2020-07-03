import collections
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        word_num = []
        for word in words:
            count = collections.Counter(word)
            word_num.append(count[sorted(count.keys())[0]])

        ans = []
        for query in queries:
            count = collections.Counter(query)
            num = count[sorted(count.keys())[0]]
            k = 0
            for w in word_num:
                if w > num:
                    k += 1
            ans.append(k)

        return ans


if __name__ == "__main__":
    print(Solution().numSmallerByFrequency(queries=["cbd"], words=["zaaaz"]))  # [1]
    print(Solution().numSmallerByFrequency(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]))  # [1,2]
