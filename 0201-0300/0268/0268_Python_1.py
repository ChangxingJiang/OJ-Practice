from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        have_zero = False
        nums_sum = 0
        nums_max = 0
        for n in nums:
            nums_sum += n
            if n == 0:
                have_zero = True
            if nums_max < n:
                nums_max = n
        expect_sum = int((1 + nums_max) * nums_max / 2)
        answer = expect_sum - nums_sum
        if answer == 0:
            if have_zero:
                return nums_max + 1
            else:
                return 0
        else:
            return answer


if __name__ == "__main__":
    print(Solution().missingNumber([0]))  # 1
    print(Solution().missingNumber([0, 1]))  # 2
    print(Solution().missingNumber([3, 0, 1]))  # 2
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
