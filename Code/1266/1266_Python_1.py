from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            x = abs(points[i + 1][0] - points[i][0])
            y = abs(points[i + 1][1] - points[i][1])
            ans += abs(x - y) + min(x, y)
        return ans


if __name__ == "__main__":
    print(Solution().minTimeToVisitAllPoints(points=[[1, 1], [3, 4], [-1, 0]]))  # 7
    print(Solution().minTimeToVisitAllPoints(points=[[3, 2], [-2, 2]]))  # 5
