from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().checkStraightLine(coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))  # True
    print(Solution().checkStraightLine(coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))  # False
