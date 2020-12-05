from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        pass


if __name__ == "__main__":
    # 12
    print(Solution().shortestDistance(maze=[
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ], start=[0, 4], destination=[4, 4]))

    # -1
    print(Solution().shortestDistance(maze=[
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ], start=[0, 4], destination=[3, 2]))
