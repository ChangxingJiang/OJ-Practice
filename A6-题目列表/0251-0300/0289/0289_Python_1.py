from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


if __name__ == "__main__":
    # [
    #   [0,0,0],
    #   [1,0,1],
    #   [0,1,1],
    #   [0,1,0]
    # ]
    matrix = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    Solution().gameOfLife(matrix)
    print(matrix)
