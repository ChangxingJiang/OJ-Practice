from typing import List


# 数组 排序


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()

        ans = 0
        last = -1
        for point in points:
            if last == -1:
                last = point[0]
            else:
                ans = max(ans, point[0] - last)
                last = point[0]

        return ans


if __name__ == "__main__":
    print(Solution().maxWidthOfVerticalArea(points=[[8, 7], [9, 9], [7, 4], [9, 7]]))  # 1
    print(Solution().maxWidthOfVerticalArea(points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))  # 3
