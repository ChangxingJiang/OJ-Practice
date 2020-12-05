from typing import List


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        pass


if __name__ == "__main__":
    # lul
    print(Solution().findShortestWay(maze=[
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0]
    ], ball=[4, 3], hole=[0, 1]))

    # impossible
    print(Solution().findShortestWay(maze=[
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0]
    ], ball=[4, 3], hole=[3, 0]))
