from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0
        for i1 in range(len(points)):
            [x1, y1] = points[i1]
            for i2 in range(i1 + 1, len(points)):
                [x2, y2] = points[i2]
                for i3 in range(i2 + 1, len(points)):
                    [x3, y3] = points[i3]
                    s = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))) / 2
                    ans = max(ans, s)
        return ans


if __name__ == "__main__":
    print(Solution().largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))  # 2
    print(Solution().largestTriangleArea([[1, 0], [0, 0], [0, 1]]))  # 0.5
    print(Solution().largestTriangleArea(
        [[35, -23], [-12, -48], [-34, -40], [21, -25], [-35, -44], [24, 1], [16, -9], [41, 4], [-36, -49], [42, -49],
         [-37, -20], [-35, 11], [-2, -36], [18, 21], [18, 8], [-24, 14], [-23, -11], [-8, 44], [-19, -3], [0, -10],
         [-21, -4], [23, 18], [20, 11], [-42, 24], [6, -19]]))  # 3627
