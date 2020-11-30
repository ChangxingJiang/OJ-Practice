from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        pass


if __name__ == "__main__":
    print(Solution().largestNumber(nums=[10, 2]))  # "210"
    print(Solution().largestNumber(nums=[3, 30, 34, 5, 9]))  # "9534330"
    print(Solution().largestNumber(nums=[1]))  # "1"
    print(Solution().largestNumber(nums=[10]))  # "10"
