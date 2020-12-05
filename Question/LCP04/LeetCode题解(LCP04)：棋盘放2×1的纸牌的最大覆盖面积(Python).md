# LeetCode题解(LCP04)：棋盘放2×1的纸牌的最大覆盖面积(Python)

题目：[原题链接](https://leetcode-cn.com/problems/broken-board-dominoes/)（困难）

标签：图、广度优先搜索、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 56ms (22.67%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < m and (x, y) not in broken

        def get_near(x, y):
            return [(x1, y1) for (x1, y1) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if is_valid(x1, y1)]

        visited = [[False] * m for _ in range(n)]
        broken = set((i, j) for (i, j) in broken)

        ans = 0

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and (i, j) not in broken:
                    # 广度优先搜索遍历当前区域
                    visited[i][j] = True
                    queue = collections.deque([(i, j)])
                    points = [(i, j)]
                    while queue:
                        i1, j1 = queue.popleft()
                        for i2, j2 in get_near(i1, j1):
                            if not visited[i2][j2]:
                                visited[i2][j2] = True
                                queue.append((i2, j2))
                                points.append((i2, j2))

                    # 思路：二分图中黑点和白点 + 贪心算法，从只有一个选择的点开始选择

                    # 构造图
                    graph = {point: set() for point in points}
                    for (i1, j1) in graph:
                        for i2, j2 in get_near(i1, j1):
                            graph[(i1, j1)].add((i2, j2))

                    # 贪心选择
                    while len(graph) >= 2:
                        for (i1, j1) in list(graph.keys()):
                            for i2, j2 in list(graph[(i1, j1)]):
                                if (i2, j2) not in graph:
                                    graph[(i1, j1)].remove((i2, j2))
                            if len(graph[(i1, j1)]) == 0:
                                del graph[(i1, j1)]

                        min_idx, min_val = (-1, -1), 5
                        for (i1, j1) in list(graph.keys()):
                            if len(graph[(i1, j1)]) < min_val:
                                min_idx, min_val = (i1, j1), len(graph[i1, j1])
                                if min_val == 1:
                                    break

                        if min_val < 5:
                            i1, j1 = min_idx
                            i2, j2 = graph[min_idx].pop()

                            del graph[(i1, j1)]
                            del graph[(i2, j2)]
                            ans += 1

        return ans
```