# LeetCode题解(0934)：最短的桥(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-bridge/)（中等）

标签：广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 324ms (16.72%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m = n = len(A)

        def _is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def _get_neighbors(x1, y1):
            return [(x2, y2) for (x2, y2) in [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
                    if _is_valid(x2, y2)]

        island = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and (i, j) not in visited:
                    this = {(i, j)}
                    queue = collections.deque([(i, j)])
                    while queue:
                        i1, j1 = queue.popleft()
                        for (i2, j2) in _get_neighbors(i1, j1):
                            if A[i2][j2] == 1 and (i2, j2) not in this:
                                queue.append((i2, j2))
                                this.add((i2, j2))
                    island.append(set(this))
                    visited |= this

        island1 = list(island[0])
        island2 = island[1]

        visited = set()
        queue = collections.deque(island1)
        step = 0
        while queue:
            for _ in range(len(queue)):
                i1, j1 = queue.popleft()
                for (i2, j2) in _get_neighbors(i1, j1):
                    if (i2, j2) in island2:
                        return step
                    if A[i2][j2] == 0 and (i2, j2) not in visited:
                        queue.append((i2, j2))
                        visited.add((i2, j2))
            step += 1
```

