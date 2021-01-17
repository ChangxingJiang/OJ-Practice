# LeetCode题解(0695)：岛屿的最大面积(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-area-of-island/)（中等）

标签：数组、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×M)$   | $O(N×M)$   | 168ms (36.22%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        ans = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or (i, j) in visited:
                    continue
                now = {(i, j)}
                queue = collections.deque([(i, j)])
                while queue:
                    for _ in range(len(queue)):
                        i1, j1 = queue.popleft()
                        for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                            if 0 <= i2 < m and 0 <= j2 < n:
                                if (i2, j2) not in now and (i2, j2) not in visited and grid[i2][j2] == 1:
                                    now.add((i2, j2))
                                    queue.append((i2, j2))
                ans = max(ans, len(now))
                visited |= now

        return ans
```

