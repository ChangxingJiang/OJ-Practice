from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        s1, s2 = len(board), len(board[0])

        ans = 0

        for i in range(s1):
            for j in range(s2):
                if board[i][j] == "X" and (i == 0 or board[i - 1][j] == ".") and (j == 0 or board[i][j - 1] == "."):
                    ans += 1

        return ans


if __name__ == "__main__":
    # 2
    print(Solution().countBattleships([
        ["X", ".", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"]
    ]))
