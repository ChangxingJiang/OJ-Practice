import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        first, end = nums[0], nums[-1]

        # 处理没有被旋转的情况
        if first < end:
            idx = bisect.bisect_right(nums, target)
            return idx - 1 if idx > 0 and nums[idx - 1] == target else -1

        elif end < target < first:
            return -1

        elif target <= end:
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= first:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return right if nums[right] == target else -1

        else:  # target >= first
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= end:
                    right = mid
                elif nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return right - 1 if nums[right - 1] == target else -1


if __name__ == "__main__":
    print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))  # 4
    print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))  # -1
    print(Solution().search(nums=[1], target=0))  # -1
    print(Solution().search(nums=[1, 3], target=1))  # 0
    print(Solution().search(nums=[3, 1], target=3))  # 0
    print(Solution().search(nums=[5, 1, 3], target=5))  # 0
