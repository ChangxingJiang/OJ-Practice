import bisect
from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        i1 = bisect.bisect_left(nums, target)  # 目标值的第1个数
        i2 = bisect.bisect_right(nums, target)  # 比目标值大的第1个数
        return i2 - i1 > len(nums) / 2


if __name__ == "__main__":
    print(Solution().isMajorityElement(nums=[2, 4, 5, 5, 5, 5, 5, 6, 6], target=5))  # True
    print(Solution().isMajorityElement(nums=[10, 100, 101, 101], target=101))  # False
