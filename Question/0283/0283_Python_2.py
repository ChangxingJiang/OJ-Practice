from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        sites = []
        for i in range(len(nums)):
            n = nums[i]
            if n != 0:
                sites.append(n)

        index = 0
        for n in sites:
            nums[index] = n
            index += 1

        for i in range(len(sites), len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(Solution().moveZeroes(nums), nums)  # [1,3,12,0,0]
    nums = [0, 0, 1]
    print(Solution().moveZeroes(nums), nums)  # [1,0,0]
