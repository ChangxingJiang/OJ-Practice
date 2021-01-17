from typing import List


# O(MNlogN)


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        # 计算列中连续相邻的长度
        con = [[0] * n for _ in range(m)]
        for j in range(n):
            con[0][j] = matrix[0][j]
            for i in range(1, m):
                con[i][j] = con[i - 1][j] + 1 if matrix[i][j] else 0

        # 计算结果
        ans = 0
        for i in range(m):
            lst = sorted(con[i], reverse=True)
            for j in range(n):
                ans = max(ans, lst[j] * (j + 1))
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
