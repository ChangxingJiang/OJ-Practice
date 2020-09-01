from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        N = len(nums)
        if N == 1:
            return str(nums[0])
        elif N == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            nums = [str(n) for n in nums]
            return nums[0] + "/(" + "/".join(nums[1:]) + ")"


if __name__ == "__main__":
    print(Solution().optimalDivision([1000, 100, 10, 2]))  # "1000/(100/10/2)"
