import bisect
from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()

        ans = -1

        for i1 in range(len(nums)):
            n1 = nums[i1]
            i2 = bisect.bisect_left(nums, k - nums[i1], lo=i1 + 1) - 1
            n2 = nums[i2]
            if i2 > i1:
                ans = max(ans, n1 + n2)

        return ans


if __name__ == "__main__":
    print(Solution().twoSumLessThanK(nums=[34, 23, 1, 24, 75, 33, 54, 8], k=60))  # 58
    print(Solution().twoSumLessThanK(nums=[10, 20, 30], k=15))  # -1
