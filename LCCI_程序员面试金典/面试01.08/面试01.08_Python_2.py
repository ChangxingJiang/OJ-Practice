from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        N1, N2 = len(matrix), len(matrix[0])

        # 检查首行的首列是否需要清空
        first_row, first_column = False, False
        if 0 in matrix[0]:
            first_row = True
        for i in range(N1):
            if matrix[i][0] == 0:
                first_column = True
                break

        # 检查中间部分是否需要清空并标记
        for i in range(N1):
            for j in range(N2):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 清空中间部分需要清空的内容
        for i in range(1, N1):
            if matrix[i][0] == 0:
                for j in range(1, N2):
                    matrix[i][j] = 0

        for j in range(1, N2):
            if matrix[0][j] == 0:
                for i in range(N1):
                    matrix[i][j] = 0

        # 清处理首行和首列
        if first_row:
            for j in range(1, N2):
                matrix[0][j] = 0

        if first_column:
            for i in range(N1):
                matrix[i][0] = 0



if __name__ == "__main__":
    # [
    #   [1,0,1],
    #   [0,0,0],
    #   [1,0,1]
    # ]
    m1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    Solution().setZeroes(m1)
    print(m1)

    # [
    #   [0,0,0,0],
    #   [0,4,5,0],
    #   [0,3,1,0]
    # ]
    m2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    Solution().setZeroes(m2)
    print(m2)
