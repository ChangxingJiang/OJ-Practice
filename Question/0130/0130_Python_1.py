import collections
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def is_valid(x, y):
            return 0 <= x < s1 and 0 <= y < s2

        def is_border(x, y):
            return (x == 0 or x == s1 - 1) or (y == 0 or y == s2 - 1)

        def get_near(x, y):
            return [(xx, yy) for (xx, yy) in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)] if
                    is_valid(xx, yy) and board[xx][yy] == "O"]

        if not board or not board[0]:
            return

        s1, s2 = len(board), len(board[0])

        visited = set()
        for i1 in range(s1):
            for i2 in range(s2):
                if board[i1][i2] == "O" and (i1, i2) not in visited:
                    this = {(i1, i2)}
                    queue = collections.deque([(i1, i2)])
                    border = is_border(i1, i2)
                    while queue:
                        j1, j2 = queue.popleft()
                        for k1, k2 in get_near(j1, j2):
                            if (k1, k2) not in visited and (k1, k2) not in this:
                                if is_border(k1, k2):
                                    border = True
                                this.add((k1, k2))
                                queue.append((k1, k2))

                    if not border:
                        for j1, j2 in this:
                            board[j1][j2] = "X"

                    visited |= this


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
