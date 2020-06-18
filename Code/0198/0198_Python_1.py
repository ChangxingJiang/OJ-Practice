from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return nums[1]
            elif i == 2:
                return nums[0] + nums[2]
            else:
                return max(helper(i - 2), helper(i - 3)) + nums[i]

        size = len(nums)
        if size == 0:
            return 0
        elif size == 1:
            return nums[0]
        else:
            return max(helper(size - 1), helper(size - 2))


if __name__ == "__main__":
    print(Solution().rob([1, 2, 3, 1]))  # 4
    print(Solution().rob([2, 7, 9, 3, 1]))  # 12
    print(Solution().rob([]))  # 0
