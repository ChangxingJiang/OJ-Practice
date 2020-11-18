from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 1
    print(Solution().numDistinctIslands([
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ]))

    # 2
    print(Solution().numDistinctIslands([
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1]
    ]))
