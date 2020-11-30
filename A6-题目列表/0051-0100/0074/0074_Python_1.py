from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass


if __name__ == "__main__":
    # True
    print(Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=3))

    # False
    print(Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=13))

    # False
    print(Solution().searchMatrix(matrix=[], target=0))
