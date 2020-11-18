from typing import List


class Solution:
    def tictactoe(self, board: List[str]) -> str:
        pass


if __name__ == "__main__":
    print(Solution().tictactoe(["O X", " XO", "X O"]))  # X
    print(Solution().tictactoe(["OOX", "XXO", "OXO"]))  # Draw
    print(Solution().tictactoe(["OOX", "XXO", "OX "]))  # Pending
