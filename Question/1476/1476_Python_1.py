from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


if __name__ == "__main__":
    sub_rectangle_queries = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
    print(sub_rectangle_queries.getValue(0, 2))  # 1
    sub_rectangle_queries.updateSubrectangle(0, 0, 3, 2, 5)
    print(sub_rectangle_queries.getValue(0, 2))  # 5
    print(sub_rectangle_queries.getValue(3, 1))  # 5
    sub_rectangle_queries.updateSubrectangle(3, 0, 3, 2, 10)
    print(sub_rectangle_queries.getValue(3, 1))  # 10
    print(sub_rectangle_queries.getValue(0, 2))  # 5
