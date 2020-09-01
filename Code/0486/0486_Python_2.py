import functools
from typing import List


class Solution:

    def PredictTheWinner(self, nums: List[int]) -> bool:
        @functools.lru_cache(None)
        def f(left, right):
            """递归函数"""
            # 处理剩下1个数的情况
            if left == right:
                return nums[left]
            # 处理剩下2个数的情况
            elif left == right - 1:
                return max(nums[left], nums[right])
            # 处理剩下3+个数的情况
            else:
                # 当前拿的数以及被对手拿去最合理的数之后的给自己剩下的数
                return max(nums[left] + min(f(left + 1, right - 1), f(left + 2, right)),
                           nums[right] + min(f(left, right - 2), f(left + 1, right - 1)))

        total_1 = f(0, len(nums) - 1)
        total_2 = sum(nums) - total_1

        return total_1 >= total_2


if __name__ == "__main__":
    print(Solution().PredictTheWinner([1, 5, 2]))  # False
    print(Solution().PredictTheWinner([1, 5, 233, 7]))  # True
    print(Solution().PredictTheWinner(
        [3606449, 6, 5, 9, 452429, 7, 9580316, 9857582, 8514433, 9, 6, 6614512, 753594, 5474165, 4, 2697293, 8, 7, 1]))  # False
