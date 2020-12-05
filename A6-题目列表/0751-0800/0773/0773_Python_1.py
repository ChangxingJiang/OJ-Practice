from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().slidingPuzzle(board=[[1, 2, 3], [4, 0, 5]]))  # 1
    print(Solution().slidingPuzzle(board=[[1, 2, 3], [5, 4, 0]]))  # -1
    print(Solution().slidingPuzzle(board=[[4, 1, 2], [5, 0, 3]]))  # 5
    print(Solution().slidingPuzzle(board=[[3, 2, 4], [1, 5, 0]]))  # 14
