from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
        return nums[left]


if __name__ == "__main__":
    print(Solution().findMin([3, 4, 5, 1, 2]))  # 1
    print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
