# LeetCode题解(面试08.02)：迷路的机器人(Python)

题目：[原题链接](https://leetcode-cn.com/problems/robot-in-a-grid-lcci/)（中等）

标签：图、深度优先搜索、回溯算法、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 56ms (72.42%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（回溯算法，可实现向四个方向走）：

```python
class Solution:
    def __init__(self):
        self.ans = []

    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return []

        height, width = len(obstacleGrid), len(obstacleGrid[0])

        visited = {(0, 0)}
        path = [(0, 0)]

        def dfs():
            x, y = path[-1]

            # 检查是否已走到终点
            if x == height - 1 and y == width - 1:
                self.ans = list(path)

            else:
                # 尝试向下走
                if x < height - 1 and obstacleGrid[x + 1][y] != 1 and (x + 1, y) not in visited:
                    path.append((x + 1, y))
                    visited.add((x + 1, y))
                    dfs()
                    path.pop()

                # 尝试向右走
                if y < width - 1 and obstacleGrid[x][y + 1] != 1 and (x, y + 1) not in visited:
                    path.append((x, y + 1))
                    visited.add((x, y + 1))
                    dfs()
                    path.pop()

                # # 尝试向上走
                # if x > 0 and obstacleGrid[x - 1][y] != 1 and (x - 1, y) not in visited:
                #     path.append((x - 1, y))
                #     visited.add((x - 1, y))
                #     dfs()
                #     path.pop()
                #
                # # 尝试向左走
                # if y > 0 and obstacleGrid[x][y - 1] != 1 and (x, y - 1) not in visited:
                #     path.append((x, y - 1))
                #     visited.add((x, y - 1))
                #     dfs()
                #     path.pop()

        dfs()

        return self.ans
```