from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        i, j, d1, d2 = 0, 0, -1, 1

        ans = []

        while len(ans) < m * n:
            ans.append(matrix[i][j])
            if 0 <= i + d1 < m and 0 <= j + d2 < n:
                i, j = i + d1, j + d2
            else:
                if j + d2 >= n:
                    i += 1
                elif i + d1 < 0:
                    j += 1
                elif i + d1 >= m:
                    j += 1
                elif j + d2 < 0:
                    i += 1
                d1, d2 = d2, d1

        return ans


if __name__ == "__main__":
    # [1,2,4,7,5,3,6,8,9]
    print(Solution().findDiagonalOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
