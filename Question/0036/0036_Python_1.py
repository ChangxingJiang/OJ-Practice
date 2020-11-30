from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            m1, m2 = set(), set()
            for j in range(9):
                if board[i][j].isnumeric():
                    if board[i][j] in m1:
                        return False
                    else:
                        m1.add(board[i][j])
                if board[j][i].isnumeric():
                    if board[j][i] in m2:
                        return False
                    else:
                        m2.add(board[j][i])

        for i in range(3):
            for j in range(3):
                m3 = set()
                for m in range(3):
                    for n in range(3):
                        if board[i * 3 + m][j * 3 + n].isnumeric():
                            if board[i * 3 + m][j * 3 + n] in m3:
                                return False
                            else:
                                m3.add(board[i * 3 + m][j * 3 + n])

        return True


if __name__ == "__main__":
    # True
    print(Solution().isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))

    # False
    print(Solution().isValidSudoku([
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))
