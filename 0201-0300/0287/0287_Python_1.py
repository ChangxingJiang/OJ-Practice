import collections
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]


if __name__ == "__main__":
    print(Solution().findDuplicate([1, 3, 4, 2, 2]))  # 2
    print(Solution().findDuplicate([3, 1, 3, 4, 2]))  # 3
