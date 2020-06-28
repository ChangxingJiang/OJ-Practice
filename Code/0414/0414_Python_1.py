from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        max1 = min(nums)
        max2 = max1
        max3 = max2
        for n in nums:
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
        return max3


if __name__ == "__main__":
    print(Solution().thirdMax([3, 2, 1]))  # 1
    print(Solution().thirdMax([1, 2]))  # 2
    print(Solution().thirdMax([2, 2, 3, 1]))  # 1
