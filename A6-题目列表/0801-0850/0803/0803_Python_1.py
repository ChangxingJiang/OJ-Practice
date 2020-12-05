from typing import List


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    # [2]
    print(Solution().hitBricks(grid=[[1, 0, 0, 0], [1, 1, 1, 0]],
                               hits=[[1, 0]]))

    # [0,0]
    print(Solution().hitBricks(grid=[[1, 0, 0, 0], [1, 1, 0, 0]],
                               hits=[[1, 1], [1, 0]]))
