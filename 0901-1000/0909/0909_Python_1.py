import collections
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])

        # 将蛇形棋转换为列表
        lst = [0]
        reverse = False
        for i in range(m - 1, -1, -1):
            if not reverse:
                lst.extend(board[i])
            else:
                lst.extend(reversed(board[i]))
            reverse = not reverse

        # 广度优先搜索
        step = 0
        visited = {1: 0}
        queue = collections.deque([1])
        while queue:
            step += 1
            for _ in range(len(queue)):
                n1 = queue.popleft()
                for n2 in range(n1 + 1, n1 + 7):
                    if n2 == m * n:
                        return step
                    if lst[n2] != -1:
                        n2 = lst[n2]
                    if n2 == m * n:
                        return step
                    if n2 not in visited or visited[n2] > step:
                        visited[n2] = step
                        queue.append(n2)

        return -1


if __name__ == "__main__":
    # 4
    print(Solution().snakesAndLadders([
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]))

    # -1
    print(Solution().snakesAndLadders([
        [1, 1, -1],
        [1, 1, 1],
        [-1, 1, 1]
    ]))

    # 2
    print(Solution().snakesAndLadders([
        [-1, -1, 19, 10, -1],
        [2, -1, -1, 6, -1],
        [-1, 17, -1, 19, -1],
        [25, -1, 20, -1, -1],
        [-1, -1, -1, -1, 15]
    ]))
