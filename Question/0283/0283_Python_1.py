from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        size = len(nums)
        i = 0
        zero = 0
        while i + zero < size:
            n = nums[i]
            if n == 0:
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]
                nums[-1] = 0
                zero += 1
            else:
                i += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(Solution().moveZeroes(nums), nums)  # [1,3,12,0,0]
    nums = [0, 0, 1]
    print(Solution().moveZeroes(nums), nums)  # [1,0,0]
