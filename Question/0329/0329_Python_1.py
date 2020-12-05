from typing import List


class Solution:
    def __init__(self):
        self.s1, self.s2 = 0, 0
        self.matrix = [[]]
        self.dp = [[]]
        self.ans = 0

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        self.s1, self.s2 = len(matrix), len(matrix[0])
        self.matrix = matrix

        self.dp = [[-1] * self.s2 for _ in range(self.s1)]

        for i1 in range(self.s1):
            for i2 in range(self.s2):
                self.dfs(i1, i2)

        return self.ans

    def dfs(self, i1, i2):
        # 处理记忆化的情况
        if self.dp[i1][i2] != -1:
            return self.dp[i1][i2]

        res = 0
        for j1, j2 in self.get_next(i1, i2):
            res = max(res, self.dfs(j1, j2))
        res += 1

        self.dp[i1][i2] = res

        self.ans = max(self.ans, res)
        return res

    def is_valid(self, i1, i2):
        return 0 <= i1 < self.s1 and 0 <= i2 < self.s2

    def get_next(self, i1, i2):
        res = []
        for j1, j2 in [(i1 - 1, i2), (i1 + 1, i2), (i1, i2 - 1), (i1, i2 + 1)]:
            if self.is_valid(j1, j2) and self.matrix[i1][i2] > self.matrix[j1][j2]:
                res.append((j1, j2))
        return res


if __name__ == "__main__":
    # 4
    print(Solution().longestIncreasingPath([
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]))

    # 4
    print(Solution().longestIncreasingPath([
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]))
