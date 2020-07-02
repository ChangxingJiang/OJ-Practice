class Solution:
    def projectionArea(self, grid):
        size = len(grid)
        ans = 0
        for i in range(size):
            max_x = 0
            max_y = 0
            for j in range(size):
                if grid[i][j]:
                    ans += 1
                max_x = max(max_x, grid[i][j])
                max_y = max(max_y, grid[j][i])
            ans += max_x + max_y
        return ans


if __name__ == "__main__":
    print(Solution().projectionArea([[2]]))  # 5
    print(Solution().projectionArea([[1, 2], [3, 4]]))  # 17
    print(Solution().projectionArea([[1, 0], [0, 2]]))  # 8
    print(Solution().projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # 14
    print(Solution().projectionArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))  # 21
