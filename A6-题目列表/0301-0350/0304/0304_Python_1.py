from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass


if __name__ == "__main__":
    obj = NumMatrix(matrix=[
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ])
    print(obj.sumRegion(2, 1, 4, 3))  # 8
    print(obj.sumRegion(1, 1, 2, 2))  # 11
    print(obj.sumRegion(1, 2, 2, 4))  # 12
