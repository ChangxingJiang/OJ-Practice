from typing import List


class BIT2D:
    def __init__(self, n1: int, n2: int):
        self.n1 = n1
        self.n2 = n2
        self._tree = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    @staticmethod
    def _lowbit(x):
        return x & (-x)

    def update(self, i: int, j: int, x: int):
        now = self.query(i, j) - self.query(i - 1, j) - self.query(i, j - 1) + self.query(i - 1, j - 1)
        self.add(i, j, x - now)

    def add(self, i: int, j: int, x: int):
        i_lst, j_lst = [], []
        while i <= self.n1:
            i_lst.append(i)
            i += BIT2D._lowbit(i)
        while j <= self.n2:
            j_lst.append(j)
            j += BIT2D._lowbit(j)
        for ii in i_lst:
            for jj in j_lst:
                self._tree[ii][jj] += x

    def query(self, i: int, j: int) -> int:
        i_lst, j_lst = [], []
        while i > 0:
            i_lst.append(i)
            i -= BIT2D._lowbit(i)
        while j > 0:
            j_lst.append(j)
            j -= BIT2D._lowbit(j)
        ans = 0
        for ii in i_lst:
            for jj in j_lst:
                ans += self._tree[ii][jj]
        return ans

    def range_query(self, i1: int, j1: int, i2: int, j2: int) -> int:
        return self.query(i2, j2) - self.query(i2, j1 - 1) - self.query(i1 - 1, j2) + self.query(i1 - 1, j1 - 1)


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            n1, n2 = 0, 0
        else:
            n1, n2 = len(matrix), len(matrix[0])
        self.BIT2D = BIT2D(n1, n2)
        for i in range(n1):
            for j in range(n2):
                self.BIT2D.update(i + 1, j + 1, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        self.BIT2D.update(row + 1, col + 1, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.BIT2D.range_query(row1 + 1, col1 + 1, row2 + 1, col2 + 1)


if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    print(obj.sumRegion(2, 1, 4, 3))  # ８
    obj.update(3, 2, 2)
    print(obj.sumRegion(2, 1, 4, 3))  # 10
    print()

    obj = NumMatrix([[]])
    print()

    obj = NumMatrix([[1, 2]])
    print(obj.sumRegion(0, 0, 0, 0))
    print(obj.sumRegion(0, 1, 0, 1))
    print(obj.sumRegion(0, 0, 0, 1))
    obj.update(0, 0, 3)
    obj.update(0, 1, 5)
    print(obj.sumRegion(0, 0, 0, 1))
