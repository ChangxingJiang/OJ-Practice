from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        more = -1
        lost = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                more = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                lost = nums[i - 1] + 1
        return [more, lost if nums[-1] == len(nums) else len(nums)]


if __name__ == "__main__":
    print(Solution().findErrorNums([1, 2, 2, 4]))  # [2,3]
    print(Solution().findErrorNums([2, 2]))  # [2,1]
    print(Solution().findErrorNums([1, 1]))  # [1,2]
    print(Solution().findErrorNums([3, 2, 3, 4, 6, 5]))  # [3,1]
