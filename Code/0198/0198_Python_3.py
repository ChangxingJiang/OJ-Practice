from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        elif size == 1:
            return nums[0]
        else:
            sum_1 = nums[0]
            sum_2 = max(nums[0], nums[1])
            for i in range(2, size):
                sum_3 = max(sum_1 + nums[i], sum_2)
                sum_1 = sum_2
                sum_2 = sum_3
            return max(sum_1, sum_2)


if __name__ == "__main__":
    print(Solution().rob([1, 2, 3, 1]))  # 4
    print(Solution().rob([2, 7, 9, 3, 1]))  # 12
    print(Solution().rob([7, 2, 7, 9, 2, 1]))  # 17
    print(Solution().rob([]))  # 0
