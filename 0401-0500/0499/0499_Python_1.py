import collections
from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
        self.maze = []
        self.hole = (0, 0)

    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        self.maze = maze
        self.hole = tuple(hole)

        ball = tuple(ball)

        visited = {ball: (0, "")}
        queue = collections.deque([(ball, 0, "")])

        ans = (float("inf"), "impossible")

        while queue:
            for _ in range(len(queue)):
                now, d1, path1 = queue.popleft()
                for next, d2, path2, res in self.move(now):
                    if res is True:
                        # print("ANS:", (d1 + d2, path1 + path2))
                        ans = min(ans, (d1 + d2, path1 + path2), key=lambda x: (x[0], x[1]))
                    elif next not in visited or (d1 + d2, path1 + path2) < visited[next]:
                        queue.append((next, d1 + d2, path1 + path2))
                        visited[next] = (d1 + d2, path1 + path2)

        return ans[1]

    def move(self, start):
        res = []

        # 向下移动
        v2 = start[0]
        hole = False
        for i in range(start[0] + 1, len(self.maze), 1):
            if (i, start[1]) == self.hole:
                hole = True
                v2 = i
                break
            if self.maze[i][start[1]] == 0:
                v2 = i
            else:
                break
        if v2 != start[0]:
            res.append(((v2, start[1]), v2 - start[0], "d", hole))

        # 向左移动
        v3 = start[1]
        hole = False
        for j in range(start[1] - 1, -1, -1):
            if (start[0], j) == self.hole:
                hole = True
                v3 = j
                break
            if self.maze[start[0]][j] == 0:
                v3 = j
            else:
                break
        if v3 != start[1]:
            res.append(((start[0], v3), start[1] - v3, "l", hole))

        # 向右移动
        v4 = start[1]
        hole = False
        for j in range(start[1] + 1, len(self.maze[0]), 1):
            if (start[0], j) == self.hole:
                hole = True
                v4 = j
                break
            if self.maze[start[0]][j] == 0:
                v4 = j
            else:
                break
        if v4 != start[1]:
            res.append(((start[0], v4), v4 - start[1], "r", hole))

        # 向上移动
        v1 = start[0]
        hole = False
        for i in range(start[0] - 1, -1, -1):
            if (i, start[1]) == self.hole:
                hole = True
                v1 = i
                break
            if self.maze[i][start[1]] == 0:
                v1 = i
            else:
                break
        if v1 != start[0]:
            res.append(((v1, start[1]), start[0] - v1, "u", hole))

        # print("MOVE:", start, "->", res, "(", v1, v2, v3, v4, ")")

        return res


if __name__ == "__main__":
    # lul
    print(Solution().findShortestWay(maze=[
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0]
    ], ball=[4, 3], hole=[0, 1]))

    # impossible
    print(Solution().findShortestWay(maze=[
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0]
    ], ball=[4, 3], hole=[3, 0]))

    # "ld"
    print(Solution().findShortestWay([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1]
    ], [0, 4], [2, 0]))

    # "r"
    print(Solution().findShortestWay([
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ], [1, 1], [1, 2]))

    # "drdrdrdldl"
    print(Solution().findShortestWay([
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    ], [2, 4], [7, 6]))
