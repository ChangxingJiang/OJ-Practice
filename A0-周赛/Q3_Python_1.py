from typing import List


# O(M×N^2)


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        # count[i][j]表示从i到j均为1的数量
        count = [[0] * m for _ in range(m)]

        for j in range(n):
            for i1 in range(m):
                for i2 in range(i1, m):
                    if matrix[i2][j] == 1:
                        count[i1][i2] += 1
                    else:
                        break

        # 计算结果
        ans = 0
        for i in range(m):
            for j in range(i, m):
                ans = max(ans, (j - i + 1) * count[i][j])
        return ans


if __name__ == "__main__":
    print(Solution().largestSubmatrix(matrix=[[0, 0, 1], [1, 1, 1], [1, 0, 1]]))  # 4
    print(Solution().largestSubmatrix(matrix=[[1, 0, 1, 0, 1]]))  # 3
    print(Solution().largestSubmatrix(matrix=[[1, 1, 0], [1, 0, 1]]))  # 2
    print(Solution().largestSubmatrix(matrix=[[0, 0], [0, 0]]))  # 0

    # 16
    print(Solution().largestSubmatrix(
        matrix=[[1, 1, 1, 0, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 0, 0, 0, 1, 1],
                [0, 1, 1, 0, 1, 1, 1, 1],
                [1, 1, 0, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0, 1, 0, 1],
                [1, 0, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 0, 1, 1],
                [1, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 1, 1],
                [1, 1, 0, 1, 1, 1, 0, 1]]))
