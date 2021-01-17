import bisect
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                idx = bisect.bisect_left(nums, nums[i] + nums[j], lo=j + 1)
                if idx == len(nums) or nums[idx] >= nums[i] + nums[j]:
                    idx -= 1
                ans += idx - j
        return ans


if __name__ == "__main__":
    print(Solution().triangleNumber([2, 2, 3, 4]))  # 3
    print(Solution().triangleNumber([1, 1, 3, 4]))  # 0
