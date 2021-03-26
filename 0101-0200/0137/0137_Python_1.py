from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            seen_once = (~seen_twice) & (seen_once ^ num)
            seen_twice = (~seen_once) & (seen_twice ^ num)
        return seen_once


if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 3, 2]))  # 3
    print(Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]))  # 99
