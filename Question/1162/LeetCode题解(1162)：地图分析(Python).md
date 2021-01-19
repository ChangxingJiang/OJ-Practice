# LeetCode题解(1162)：地图分析(Python)

题目：[原题链接](https://leetcode-cn.com/problems/as-far-from-land-as-possible/)（中等）

标签：广度优先搜索、图

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 532ms (61.37%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def _is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def _get_neighbors(x1, y1):
            return [(x2, y2) for (x2, y2) in [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
                    if _is_valid(x2, y2)]

        visited = set()
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))

        if len(visited) == m * n:
            return -1

        step = 0
        while queue:
            for _ in range(len(queue)):
                i1, j1 = queue.popleft()
                for i2, j2 in _get_neighbors(i1, j1):
                    if (i2, j2) not in visited:
                        queue.append((i2, j2))
                        visited.add((i2, j2))
            if not queue:
                return step
            else:
                step += 1

        return -1
```

