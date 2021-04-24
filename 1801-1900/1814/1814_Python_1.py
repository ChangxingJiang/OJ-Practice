import collections
from typing import List


class Solution:
    _MOD = 10 ** 9 + 7

    def countNicePairs(self, nums: List[int]) -> int:
        nums = [num - int(str(num)[::-1]) for num in nums]
        count = collections.Counter(nums)
        return sum(value * (value - 1) // 2 for value in count.values()) % self._MOD


if __name__ == "__main__":
    print(Solution().countNicePairs([42, 11, 1, 97]))  # 2
    print(Solution().countNicePairs([13, 10, 35, 24, 76]))  # 4
