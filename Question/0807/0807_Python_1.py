from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = [0] * m, [0] * n

        for i in range(m):
            for j in range(n):
                rows[i] = max(rows[i], grid[i][j])
                cols[j] = max(cols[j], grid[i][j])

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += min(rows[i], cols[j]) - grid[i][j]
        return ans


if __name__ == "__main__":
    # 35
    print(Solution().maxIncreaseKeepingSkyline(grid=[[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
