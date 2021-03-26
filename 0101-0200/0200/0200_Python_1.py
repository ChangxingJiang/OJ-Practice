from typing import List


class DSU:
    def __init__(self, n):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i):
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_valid(x, y):
            return 0 <= x < s1 and 0 <= y < s2

        def get_near(x, y):
            return [(xx, yy) for (xx, yy) in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)] if is_valid(xx, yy)]

        s1, s2 = len(grid), len(grid[0])

        dsu = DSU(s1 * s2)

        island = []
        for i1 in range(s1):
            for i2 in range(s2):
                if grid[i1][i2] == "1":
                    idx1 = i1 * s2 + i2

                    # 如果当前岛屿未被记录，则记录当前岛屿
                    if dsu.find(idx1) == idx1:
                        island.append(idx1)

                    for j1, j2 in get_near(i1, i2):
                        if grid[j1][j2] == "1":
                            idx2 = j1 * s2 + j2
                            dsu.union(idx1, idx2)

        return len(set(dsu.find(idx) for idx in island))


if __name__ == "__main__":
    # 1
    print(Solution().numIslands(grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))

    # 3
    print(Solution().numIslands(grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))
