from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        # 沿左上-右下对角线翻转
        for i in range(N):
            for j in range(i + 1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 水平翻转
        for i in range(N):
            for j in range(N // 2):
                matrix[i][j], matrix[i][N - j - 1] = matrix[i][N - j - 1], matrix[i][j]


if __name__ == "__main__":
    # [
    #   [7,4,1],
    #   [8,5,2],
    #   [9,6,3]
    # ]
    m1 = matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    Solution().rotate(m1)
    print(m1)

    # [
    #   [15,13, 2, 5],
    #   [14, 3, 4, 1],
    #   [12, 6, 8, 9],
    #   [16, 7,10,11]
    # ]
    m2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    Solution().rotate(m2)
    print(m2)
