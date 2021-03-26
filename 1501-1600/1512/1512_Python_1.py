import collections
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = collections.Counter()
        ans = 0
        for n in nums:
            ans += count[n]
            count[n] += 1
        return ans


if __name__ == "__main__":
    print(Solution().numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]))  # 4
    print(Solution().numIdenticalPairs(nums=[1, 1, 1, 1]))  # 6
    print(Solution().numIdenticalPairs(nums=[1, 2, 3]))  # 0
