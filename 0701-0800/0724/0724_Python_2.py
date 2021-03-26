from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        differ = sum(nums)
        for i in range(len(nums)):
            if i > 0:
                differ -= nums[i] + nums[i - 1]
            else:
                differ -= nums[i]
            if differ == 0:
                return i
        else:
            return -1


if __name__ == "__main__":
    print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))  # 3
    print(Solution().pivotIndex([1, 2, 3]))  # -1
    print(Solution().pivotIndex([-1, -1, 0, 1, 1, 0]))  # 5
