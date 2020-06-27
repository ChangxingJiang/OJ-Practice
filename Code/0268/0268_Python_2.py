from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_max = len(nums)
        nums_sum = 0
        for n in nums:
            nums_sum += n
        expect_sum = int((1 + nums_max) * nums_max / 2)
        return expect_sum - nums_sum


if __name__ == "__main__":
    print(Solution().missingNumber([0]))  # 1
    print(Solution().missingNumber([0, 1]))  # 2
    print(Solution().missingNumber([3, 0, 1]))  # 2
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
