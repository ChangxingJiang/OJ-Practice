from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        num0 = nums.count(0)
        num1 = nums.count(1)

        for i in range(num0):
            nums[i] = 0
        for i in range(num0, num0 + num1):
            nums[i] = 1
        for i in range(num0 + num1, len(nums)):
            nums[i] = 2


if __name__ == "__main__":
    lst = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(lst)
    print(lst)
