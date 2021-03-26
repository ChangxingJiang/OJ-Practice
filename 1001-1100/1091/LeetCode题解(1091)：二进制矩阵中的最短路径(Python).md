# LeetCode题解(1091)：二进制矩阵中的最短路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/)（中等）

标签：广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 1120ms (5.01%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def _is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def _get_neighbors(x1, y1):
            return [(x2, y2) for (x2, y2) in [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1),
                                              (x1 - 1, y1 - 1), (x1 + 1, y1 + 1), (x1 + 1, y1 - 1), (x1 - 1, y1 + 1)]
                    if _is_valid(x2, y2)]

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        if m == 1 and n == 1:
            return 1

        visited = {(0, 0)}
        queue = collections.deque([(0, 0)])
        step = 1
        while queue:
            step += 1
            for _ in range(len(queue)):
                i1, j1 = queue.popleft()
                for i2, j2 in _get_neighbors(i1, j1):
                    if (i2, j2) == (m - 1, n - 1):
                        return step
                    if grid[i2][j2] == 0 and (i2, j2) not in visited:
                        visited.add((i2, j2))
                        queue.append((i2, j2))

        return -1
```

