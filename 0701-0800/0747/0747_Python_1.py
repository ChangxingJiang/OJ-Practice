from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max1 = -1
        max2 = -1
        idx = -1
        for i in range(len(nums)):
            n = nums[i]
            if n > max1:
                max2 = max1
                max1 = n
                idx = i
            elif n > max2:
                max2 = n
        if max1 >= max2 * 2:
            return idx
        else:
            return -1


if __name__ == "__main__":
    print(Solution().dominantIndex([3, 6, 1, 0]))  # 1
    print(Solution().dominantIndex([1, 2, 3, 4]))  # -1
    print(Solution().dominantIndex([1]))  # 0
