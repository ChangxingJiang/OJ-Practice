from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        s = sum(map(sum, grid))
        m = len(grid) >> 1
        if not s or not m or s == 4 * m * m:
            return Node(bool(s), True, None, None, None, None)
        else:
            return Node(True, False,
                        self.construct([g[: m] for g in grid[: m]]),
                        self.construct([g[m:] for g in grid[: m]]),
                        self.construct([g[: m] for g in grid[m:]]),
                        self.construct([g[m:] for g in grid[m:]]))


if __name__ == "__main__":
    pass
