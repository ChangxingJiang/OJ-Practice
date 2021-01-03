import collections
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        s1, s2 = len(target), len(arr)

        count = collections.defaultdict(list)


if __name__ == "__main__":
    print(Solution().minOperations(target=[5, 1, 3], arr=[9, 4, 2, 3, 4]))  # 2
    print(Solution().minOperations(target=[6, 4, 8, 1, 3, 2], arr=[4, 7, 6, 2, 3, 8, 6, 1]))  # 3
