from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        for n in nums:
            if n > max1:
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n
        return (max1 - 1) * (max2 - 1)


if __name__ == "__main__":
    print(Solution().maxProduct(nums=[3, 4, 5, 2]))  # 12
    print(Solution().maxProduct(nums=[1, 5, 4, 5]))  # 16
    print(Solution().maxProduct(nums=[3, 7]))  # 12
