from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        elif size == 1:
            return nums[0]
        elif size == 2:
            return max(nums[0], nums[1])
        else:
            sum_1 = nums[0]  # 取得第i-3个数的最大值
            sum_2 = nums[1]  # 取得第i-2个数的最大值
            sum_3 = nums[0] + nums[2]  # 取得第i-1个数的最大值
            for i in range(3, size):
                n = nums[i]
                sum_4 = max(sum_1 + n, sum_2 + n)  # 取得第i个数的最大值
                sum_1 = sum_2
                sum_2 = sum_3
                sum_3 = sum_4
            return max(sum_2, sum_3)


if __name__ == "__main__":
    print(Solution().rob([1, 2, 3, 1]))  # 4
    print(Solution().rob([2, 7, 9, 3, 1]))  # 12
    print(Solution().rob([]))  # 0
