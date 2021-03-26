import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        lst = heapq.nsmallest(k, count.keys(), key=lambda x: (-count[x], x))
        return lst


if __name__ == "__main__":
    # ["i", "love"]
    print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k=2))

    # ["the", "is", "sunny", "day"]
    print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4))

    # ["i", "love", "coding"]
    print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k=3))
