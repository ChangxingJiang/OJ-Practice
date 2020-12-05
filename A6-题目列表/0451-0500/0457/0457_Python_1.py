from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().circularArrayLoop([2, -1, 1, 2, 2]))  # True
    print(Solution().circularArrayLoop([-1, 2]))  # False
    print(Solution().circularArrayLoop([-2, 1, -1, -2, -2]))  # False
