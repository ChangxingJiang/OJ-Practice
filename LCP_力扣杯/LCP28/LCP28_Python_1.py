import bisect
from typing import List


class Solution:
    _MOD = 1000000007

    def purchasePlans(self, nums: List[int], target: int) -> int:
        size = len(nums)

        nums.sort()

        ans = 0

        for i in range(size):
            j = bisect.bisect_right(nums, target - nums[i])
            if j > i:
                ans += (j - i - 1)

        return ans % self._MOD


if __name__ == "__main__":
    print(Solution().purchasePlans(nums=[2, 5, 3, 5], target=6))  # 1
    print(Solution().purchasePlans(nums=[2, 2, 1, 9], target=10))  # 4
    print(Solution().purchasePlans(nums=[1, 3, 5], target=10))  # 3
