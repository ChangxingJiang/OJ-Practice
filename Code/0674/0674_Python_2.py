from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maximum = num = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                num += 1
                maximum = max(maximum, num)
            else:
                num = 1
        return maximum


if __name__ == "__main__":
    print(Solution().findLengthOfLCIS([1, 3, 5, 4, 7]))  # 3
    print(Solution().findLengthOfLCIS([2, 2, 2, 2, 2]))  # 1
    print(Solution().findLengthOfLCIS([1, 3, 5, 4, 2, 3, 4, 5]))  # 4
