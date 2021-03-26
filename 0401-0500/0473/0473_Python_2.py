import functools
from typing import List


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        size, sum_of_sides = len(nums), sum(nums)
        possible_side = sum_of_sides // 4  # 计算可能的边长

        # 处理边不够、边长不是整数、存在超长边的情况
        if size < 4 or sum(nums) % 4 != 0 or max(nums) > possible_side:
            return False

        @functools.lru_cache(None)
        def recurse(mask, total, sides_done):
            # 处理已经完成3条边的情况
            if sides_done == 3:
                return True

            if total == possible_side:
                return recurse(mask, 0, sides_done + 1)

            for i in range(size):
                if total + nums[i] <= possible_side and not mask & (1 << i):
                    if recurse(mask | (1 << i), total + nums[i], sides_done):
                        return True

            return False

        return recurse(0, 0, 0)


if __name__ == "__main__":
    print(Solution().makesquare([1, 1, 2, 2, 2]))  # True
    print(Solution().makesquare([3, 3, 3, 3, 4]))  # False
