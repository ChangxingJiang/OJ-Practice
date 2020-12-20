from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        pass


if __name__ == "__main__":
    # 4
    print(Solution().maxArea(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]))

    # 6
    print(Solution().maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]))

    # 9
    print(Solution().maxArea(h=5, w=4, horizontalCuts=[3], verticalCuts=[3]))
