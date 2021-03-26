import collections
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and board[x][y] == "E"

        def is_mine(x, y):
            return 0 <= x < m and 0 <= y < n and board[x][y] == "M"

        def get_neighbors(x1, y1):
            return [(x2, y2) for x2, y2 in
                    [(x1 + 1, y1), (x1 + 1, y1 - 1), (x1 + 1, y1 + 1), (x1, y1 - 1), (x1, y1 + 1), (x1 - 1, y1 - 1),
                     (x1 - 1, y1), (x1 - 1, y1 + 1)] if is_valid(x2, y2)]

        def get_near(x1, y1):
            return len([(x2, y2) for x2, y2 in
                        [(x1 + 1, y1), (x1 + 1, y1 - 1), (x1 + 1, y1 + 1), (x1, y1 - 1), (x1, y1 + 1), (x1 - 1, y1 - 1),
                         (x1 - 1, y1), (x1 - 1, y1 + 1)] if is_mine(x2, y2)])

        m, n = len(board), len(board[0])

        # 如果直接挖到地雷
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        # 如果没有挖到地雷
        queue = collections.deque([(click[0], click[1])])
        visited = {(click[0], click[1])}
        while queue:
            for _ in range(len(queue)):
                i1, j1 = queue.popleft()
                num = get_near(i1, j1)
                board[i1][j1] = str(num) if num > 0 else "B"

                if num == 0:
                    for i2, j2 in get_neighbors(i1, j1):
                        if (i2, j2) not in visited:
                            visited.add((i2, j2))
                            queue.append((i2, j2))

        return board


if __name__ == "__main__":
    # [['B', '1', 'E', '1', 'B'],
    #  ['B', '1', 'M', '1', 'B'],
    #  ['B', '1', '1', '1', 'B'],
    #  ['B', 'B', 'B', 'B', 'B']]
    print(Solution().updateBoard([
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'M', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E']
    ], [3, 0]))

    # [['B', '1', 'E', '1', 'B'],
    #  ['B', '1', 'X', '1', 'B'],
    #  ['B', '1', '1', '1', 'B'],
    #  ['B', 'B', 'B', 'B', 'B']]
    print(Solution().updateBoard([
        ['B', '1', 'E', '1', 'B'],
        ['B', '1', 'M', '1', 'B'],
        ['B', '1', '1', '1', 'B'],
        ['B', 'B', 'B', 'B', 'B']
    ], [1, 2]))
