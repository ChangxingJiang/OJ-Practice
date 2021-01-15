from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 处理数组长度为1的情况
        if len(nums) == 1:
            return 0

        # 处理两侧边缘就是峰值的情况
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        # 二分查找
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    print(Solution().findPeakElement(nums=[1, 2, 3, 1]))  # 2
    print(Solution().findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4]))  # 1或5
    print(Solution().findPeakElement(nums=[1, 2]))  # 1
    print(Solution().findPeakElement(nums=[1, 3, 2, 1]))  # 1
