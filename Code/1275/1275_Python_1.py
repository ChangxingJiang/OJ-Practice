from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        A = [0 for _ in range(9)]
        B = [0 for _ in range(9)]
        step = 0
        for move in moves:
            if step % 2 == 0:
                A[move[0] * 3 + move[1]] = 1
            else:
                B[move[0] * 3 + move[1]] = 1
            step += 1

        maybes = {(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)}
        for maybe in maybes:
            if A[maybe[0]] == 1 and A[maybe[1]] == 1 and A[maybe[2]] == 1:
                return "A"
            elif B[maybe[0]] == 1 and B[maybe[1]] == 1 and B[maybe[2]] == 1:
                return "B"
        if step == 9:
            return "Draw"
        else:
            return "Pending"


if __name__ == "__main__":
    print(Solution().tictactoe(moves=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))  # A
    print(Solution().tictactoe(moves=[[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))  # B
    print(Solution().tictactoe(moves=[[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]))  # Draw
    print(Solution().tictactoe(moves=[[0, 0], [1, 1]]))  # Pending
