from typing import List


# 数组
# O(N)


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        ans = 0
        for i in range(n):
            ans += mat[i][i] + mat[i][n - 1 - i] if i != n - 1 - i else mat[i][i]

        return ans


if __name__ == "__main__":
    # 25
    print(Solution().diagonalSum(mat=[[1, 2, 3],
                                      [4, 5, 6],
                                      [7, 8, 9]]))

    # 8
    print(Solution().diagonalSum(mat=[[1, 1, 1, 1],
                                      [1, 1, 1, 1],
                                      [1, 1, 1, 1],
                                      [1, 1, 1, 1]]))

    # 5
    print(Solution().diagonalSum(mat=[[5]]))
