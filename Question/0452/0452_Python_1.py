from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        now = points[0][1]
        ans = 0

        for i1, i2 in points:
            if i1 > now:
                now = i2
                ans += 1

        return ans + 1


if __name__ == "__main__":
    print(Solution().findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))  # 2
    print(Solution().findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]))  # 4
    print(Solution().findMinArrowShots(points=[[1, 2], [2, 3], [3, 4], [4, 5]]))  # 2
    print(Solution().findMinArrowShots(points=[[1, 2]]))  # 1
    print(Solution().findMinArrowShots(points=[[2, 3], [2, 3]]))  # 1
    print(Solution().findMinArrowShots(points=[[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]))  # 2
