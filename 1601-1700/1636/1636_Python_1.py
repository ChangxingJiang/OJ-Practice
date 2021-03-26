import collections
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        nums.sort(key=lambda x: (count[x], -x))
        return nums


if __name__ == "__main__":
    print(Solution().frequencySort(nums=[1, 1, 2, 2, 2, 3]))  # [3,1,1,2,2,2]
    print(Solution().frequencySort(nums=[2, 3, 1, 3, 2]))  # [1,3,3,2,2]
    print(Solution().frequencySort(nums=[-1, 1, -6, 4, 5, -6, 1, 4, 1]))  # [5,-1,4,4,-6,-6,1,1,1]
