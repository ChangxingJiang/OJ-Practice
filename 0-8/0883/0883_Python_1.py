from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().projectionArea([[2]]))  # 5
    print(Solution().projectionArea([[1, 2], [3, 4]]))  # 17
    print(Solution().projectionArea([[1, 0], [0, 2]]))  # 8
    print(Solution().projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # 14
    print(Solution().projectionArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))  # 21
