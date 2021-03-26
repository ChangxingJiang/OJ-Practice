from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for d in range(-m + 1, n):
            if d < 0:
                i0, j0, num = -d, 0, min(m + d, n)
            else:
                i0, j0, num = 0, d, min(n - d, m)

            lst = []
            for k in range(num):
                i1, j1 = i0 + k, j0 + k
                lst.append(mat[i1][j1])
            lst.sort()
            for k in range(num):
                i1, j1 = i0 + k, j0 + k
                mat[i1][j1] = lst[k]

        return mat


if __name__ == "__main__":
    # [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
    print(Solution().diagonalSort(mat=[[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))
