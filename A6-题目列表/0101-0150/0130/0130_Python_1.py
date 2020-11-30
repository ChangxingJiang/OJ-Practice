from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


if __name__ == "__main__":
    matrix = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    Solution().solve(matrix)
    print(matrix)
    # X X X X
    # X X X X
    # X X X X
    # X O X X
