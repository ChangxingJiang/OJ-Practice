from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def _is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def _get_neighbors(x1, y1):
            return [(x2, y2) for (x2, y2) in [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
                    if _is_valid(x2, y2)]

        waiting = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    waiting.add((i, j))

        ans = 0

        for i1, j1 in waiting:
            def dfs(ii1, jj1, vv1):
                res = vv1
                for ii2, jj2 in _get_neighbors(ii1, jj1):
                    vv2 = vv1 + grid[ii2][jj2]
                    if grid[ii2][jj2] > 0 and (ii2, jj2) not in visited:
                        visited.add((ii2, jj2))
                        res = max(res, dfs(ii2, jj2, vv2))
                        visited.remove((ii2, jj2))
                return res

            visited = {(i1, j1)}
            ans = max(ans, dfs(i1, j1, grid[i1][j1]))

        return ans


if __name__ == "__main__":
    # 24
    print(Solution().getMaximumGold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]]))

    # 28
    print(Solution().getMaximumGold(grid=[[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))
