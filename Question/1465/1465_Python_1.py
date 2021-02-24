from typing import List


class Solution:
    _MOD = 10 ** 9 + 7

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        width, height = 0, 0

        horizontalCuts.sort()
        horizontalCuts.append(h)
        last = 0
        for n in horizontalCuts:
            height = max(height, n - last)
            last = n

        verticalCuts.sort()
        verticalCuts.append(w)
        last = 0
        for n in verticalCuts:
            width = max(width, n - last)
            last = n

        return width * height % self._MOD


if __name__ == "__main__":
    # 4
    print(Solution().maxArea(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]))

    # 6
    print(Solution().maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]))

    # 9
    print(Solution().maxArea(h=5, w=4, horizontalCuts=[3], verticalCuts=[3]))
