from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        s1, s2 = len(grid), len(grid[0])

        ans = 0

        for i1 in range(s1):
            for i2 in range(s2):
                if grid[i1][i2] == "0":
                    count = 0
                    for i3 in range(i1 - 1, -1, -1):
                        if grid[i3][i2] == "W":
                            break
                        if grid[i3][i2] == "E":
                            count += 1
                    for i3 in range(i1 + 1, s1, 1):
                        if grid[i3][i2] == "W":
                            break
                        if grid[i3][i2] == "E":
                            count += 1
                    for i4 in range(i2 - 1, -1, -1):
                        if grid[i1][i4] == "W":
                            break
                        if grid[i1][i4] == "E":
                            count += 1
                    for i4 in range(i2 + 1, s2, 1):
                        if grid[i1][i4] == "W":
                            break
                        if grid[i1][i4] == "E":
                            count += 1
                    ans = max(ans, count)

        return ans


if __name__ == "__main__":
    # 3
    print(Solution().maxKilledEnemies([
        ["0", "E", "0", "0"],
        ["E", "0", "W", "E"],
        ["0", "E", "0", "0"]]))
