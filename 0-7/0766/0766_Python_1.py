from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))  # True
    print(Solution().isToeplitzMatrix([[1, 2], [2, 2]]))  # False
