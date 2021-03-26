import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = collections.Counter({0: 1})

        ans = 0

        last = 0
        for n in nums:
            last += n
            ans += hashmap[last - k]
            hashmap[last] += 1

        return ans


if __name__ == "__main__":
    print(Solution().subarraySum(nums=[1, 1, 1], k=2))  # 2
    print(Solution().subarraySum(nums=[1], k=0))  # 0
