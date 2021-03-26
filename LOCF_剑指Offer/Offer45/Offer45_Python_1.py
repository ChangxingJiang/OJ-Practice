import functools
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]

        def sort_key(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        nums.sort(key=functools.cmp_to_key(sort_key))

        return "".join(nums)


if __name__ == "__main__":
    print(Solution().minNumber([10, 2]))  # "102"
    print(Solution().minNumber([3, 30, 34, 5, 9]))  # "3033459"
