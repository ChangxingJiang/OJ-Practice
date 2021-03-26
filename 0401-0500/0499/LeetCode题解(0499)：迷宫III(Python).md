# LeetCode题解(0499)：迷宫III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/the-maze-iii/)（困难）

标签：广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 84ms (53.06%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.visited = set()
        self.maze = []
        self.hole = (0, 0)

    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        self.maze = maze
        self.hole = tuple(hole)

        ball = tuple(ball)

        visited = {ball: 0}
        queue = collections.deque([(ball, "")])

        ans = "impossible"

        while queue:
            for _ in range(len(queue)):
                now, path1 = queue.popleft()
                for next, path2, res in self.move(now):
                    if res is True:
                        if ans != "impossible":
                            ans = min(ans, path1 + path2)
                        else:
                            ans = path1 + path2
                    elif next not in visited:
                        queue.append((next, path1 + path2))
                        visited[next] = path1 + path2

        return ans

    def move(self, start):
        res = []

        # 向下移动
        v2 = start[0]
        hole = False
        for i in range(start[0] + 1, len(self.maze), 1):
            if (i, start[1]) == self.hole:
                hole = True
            if self.maze[i][start[1]] == 0:
                v2 = i
            else:
                break
        if v2 != start[0]:
            res.append(((v2, start[1]), "d", hole))

        # 向左移动
        v3 = start[1]
        hole = False
        for j in range(start[1] - 1, -1, -1):
            if (start[0], j) == self.hole:
                hole = True
            if self.maze[start[0]][j] == 0:
                v3 = j
            else:
                break
        if v3 != start[1]:
            res.append(((start[0], v3), "l", hole))

        # 向右移动
        v4 = start[1]
        hole = False
        for j in range(start[1] + 1, len(self.maze[0]), 1):
            if (start[0], j) == self.hole:
                hole = True
            if self.maze[start[0]][j] == 0:
                v4 = j
            else:
                break
        if v4 != start[1]:
            res.append(((start[0], v4), "r", hole))

        # 向上移动
        v1 = start[0]
        hole = False
        for i in range(start[0] - 1, -1, -1):
            if (i, start[1]) == self.hole:
                hole = True
            if self.maze[i][start[1]] == 0:
                v1 = i
            else:
                break
        if v1 != start[0]:
            res.append(((v1, start[1]), "u", hole))

        # print("MOVE:", start, "->", res, "(", v1, v2, v3, v4, ")")

        return res
```