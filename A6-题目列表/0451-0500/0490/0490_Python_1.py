from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        pass


if __name__ == "__main__":
    # True
    print(Solution().hasPath(
        maze=[
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]
        ],
        start=[0, 4],
        destination=[4, 4]
    ))

    # True
    print(Solution().hasPath(
        maze=[
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]
        ],
        start=[0, 4],
        destination=[3, 2]
    ))
