from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 2
    print(Solution().movesToChessboard(board=[[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]))

    # 0
    print(Solution().movesToChessboard(board=[[0, 1], [1, 0]]))

    # -1
    print(Solution().movesToChessboard(board=[[1, 0], [1, 0]]))
