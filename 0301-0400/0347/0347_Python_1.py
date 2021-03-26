import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [elem[0] for elem in collections.Counter(nums).most_common(k)]


if __name__ == "__main__":
    print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))  # [1,2]
    print(Solution().topKFrequent(nums=[1], k=1))  # [1]
