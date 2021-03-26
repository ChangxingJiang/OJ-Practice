from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx0 = 0
        idx1 = len(nums)
        while idx0 < idx1:
            mid = int((idx1 + idx0) / 2)
            if target < nums[mid]:
                idx1 = mid
            elif target > nums[mid]:
                idx0 = mid + 1
            else:
                return mid
        else:
            return -1


if __name__ == "__main__":
    print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9))  # 4
    print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=2))  # -1
