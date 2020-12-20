from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 1
    print(Solution().minimumMoves(grid=[[0, 0, 0, 0, 0, 1],
                                        [1, 1, 0, 0, 1, 0],
                                        [0, 0, 0, 0, 1, 1],
                                        [0, 0, 1, 0, 1, 0],
                                        [0, 1, 1, 0, 0, 0],
                                        [0, 1, 1, 0, 0, 0]]))

    # 9
    print(Solution().minimumMoves(grid=[[0, 0, 1, 1, 1, 1],
                                        [0, 0, 0, 0, 1, 1],
                                        [1, 1, 0, 0, 0, 1],
                                        [1, 1, 1, 0, 0, 1],
                                        [1, 1, 1, 0, 0, 1],
                                        [1, 1, 1, 0, 0, 0]]))
