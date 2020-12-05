from typing import List


class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isConvex([[0, 0], [0, 1], [1, 1], [1, 0]]))  # True
    print(Solution().isConvex([[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]))  # False
