from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        N1, N2 = len(matrix), len(matrix[0])

        remove_x = set()
        remove_y = set()

        for i in range(N1):
            for j in range(N2):
                if matrix[i][j] == 0:
                    remove_x.add(i)
                    remove_y.add(j)

        for i in remove_x:
            for j in range(N2):
                matrix[i][j] = 0

        for j in remove_y:
            for i in range(N1):
                matrix[i][j] = 0


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
