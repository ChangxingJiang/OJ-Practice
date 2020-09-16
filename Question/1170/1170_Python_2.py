import bisect
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words = [word.count(min(word)) for word in words]
        words.sort()

        ans = []
        for query in queries:
            num = query.count(min(query))
            count = len(words) - bisect.bisect_right(words, num)
            ans.append(count)

        return ans


if __name__ == "__main__":
    print(Solution().numSmallerByFrequency(queries=["cbd"], words=["zaaaz"]))  # [1]
    print(Solution().numSmallerByFrequency(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]))  # [1,2]
