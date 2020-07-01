from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        if all([m >= 2 * n for n in nums if n != m]):
            return nums.index(m)
        else:
            return -1


if __name__ == "__main__":
    print(Solution().dominantIndex([3, 6, 1, 0]))  # 1
    print(Solution().dominantIndex([1, 2, 3, 4]))  # -1
    print(Solution().dominantIndex([1]))  # 0
