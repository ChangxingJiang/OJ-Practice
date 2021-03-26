from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        size = len(grid)

        max_x = [0 for _ in range(size)]
        max_y = [0 for _ in range(size)]
        ans = 0
        for i in range(size):
            for j in range(size):
                if grid[i][j] > 0:
                    ans += 1
                    max_x[i] = max(max_x[i], grid[i][j])
                    max_y[j] = max(max_y[j], grid[i][j])
        return ans + sum(max_x) + sum(max_y)


if __name__ == "__main__":
    print(Solution().projectionArea([[2]]))  # 5
    print(Solution().projectionArea([[1, 2], [3, 4]]))  # 17
    print(Solution().projectionArea([[1, 0], [0, 2]]))  # 8
    print(Solution().projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # 14
    print(Solution().projectionArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))  # 21
