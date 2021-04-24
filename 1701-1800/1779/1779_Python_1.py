from typing import List


class Solution:
    def nearestValidPoint(self, x1: int, y1: int, points: List[List[int]]) -> int:
        min_distance = float("inf")
        ans = -1
        for i in range(len(points)):
            x2, y2 = points[i]
            if x1 == x2 or y1 == y2:
                distance = abs(x1 - x2) + abs(y1 - y2)
                if distance < min_distance:
                    min_distance = distance
                    ans = i
        return ans


if __name__ == "__main__":
    print(Solution().nearestValidPoint(x1=3, y1=4, points=[[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))  # 2
    print(Solution().nearestValidPoint(x1=3, y1=4, points=[[3, 4]]))  # 0
    print(Solution().nearestValidPoint(x1=3, y1=4, points=[[2, 3]]))  # -1
