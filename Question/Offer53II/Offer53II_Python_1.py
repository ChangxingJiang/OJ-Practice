from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid
        return nums[left] - 1 if left < len(nums) else len(nums)


if __name__ == "__main__":
    print(Solution().missingNumber([0, 1, 3]))  # 2
    print(Solution().missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 9]))  # 8
    print(Solution().missingNumber([0]))  # 1
