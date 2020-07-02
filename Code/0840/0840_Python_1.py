from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        x = len(grid)
        y = len(grid[0])
        if x < 3 or y < 3:
            return 0

        ans = 0
        for i in range(x - 2):
            for j in range(x - 2):
                # 检查是否仅包含1-9
                num_list = {grid[i][j], grid[i][j + 1], grid[i][j + 2], grid[i + 1][j], grid[i + 1][j + 1],
                            grid[i + 1][j + 2], grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]}
                if not (1 in num_list and 2 in num_list and 3 in num_list and 4 in num_list and
                        5 in num_list and 6 in num_list and 7 in num_list and 8 in num_list and 9 in num_list):
                    continue

                # 检查行列对角线加和是否正确（枚举8条线）
                num = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
                if grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1] != num:
                    continue
                if grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2] != num:
                    continue
                if grid[i][j] + grid[i][j + 1] + grid[i][j + 2] != num:
                    continue
                if grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2] != num:
                    continue
                if grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2] != num:
                    continue
                if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != num:
                    continue
                if grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2] != num:
                    continue

                ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().numMagicSquaresInside([[4, 3, 8, 4],
                                            [9, 5, 1, 9],
                                            [2, 7, 6, 2]]))  # 1
