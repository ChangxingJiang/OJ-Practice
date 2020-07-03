from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        pass


if __name__ == "__main__":
    print(Solution().tictactoe(moves=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))  # A
    print(Solution().tictactoe(moves=[[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))  # B
    print(Solution().tictactoe(moves=[[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]))  # Draw
    print(Solution().tictactoe(moves=[[0, 0], [1, 1]]))  # Bending
