from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]

        total = 1
        zero_num = 0
        for num in nums:
            if num == 0:
                zero_num += 1
            else:
                total *= num

        if zero_num >= 2:
            return [0] * len(nums)

        if zero_num == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = total
                else:
                    nums[i] = 0
            return nums

        else:
            for i in range(len(nums)):
                nums[i] = total // nums[i]
            return nums


if __name__ == "__main__":
    #  [24,12,8,6]
    print(Solution().productExceptSelf([1, 2, 3, 4]))

    # [0,0]
    print(Solution().productExceptSelf([0, 0]))
