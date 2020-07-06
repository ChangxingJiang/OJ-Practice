from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        for (x3, y3) in coordinates[2:]:
            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                return False
        else:
            return True


if __name__ == "__main__":
    print(Solution().checkStraightLine(coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))  # True
    print(Solution().checkStraightLine(coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))  # False
