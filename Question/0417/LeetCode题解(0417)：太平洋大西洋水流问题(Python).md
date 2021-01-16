# LeetCode题解(0417)：太平洋大西洋水流问题(Python)

题目：[原题链接](https://leetcode-cn.com/problems/pacific-atlantic-water-flow/)（中等）

标签：深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 352ms (41.58%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])

        def _is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def _get_near(x, y):
            return [(xx, yy) for (xx, yy) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if _is_valid(xx, yy)]

        queue1 = collections.deque([])
        visited1 = set()
        queue2 = collections.deque([])
        visited2 = set()

        # 标记地图边缘位置
        for i in range(m):
            queue1.append((i, 0))
            visited1.add((i, 0))
            queue2.append((i, n - 1))
            visited2.add((i, n - 1))
        for j in range(n):
            queue1.append((0, j))
            visited1.add((0, j))
            queue2.append((m - 1, j))
            visited2.add((m - 1, j))

        # 标记太平洋
        while queue1:
            i1, j1 = queue1.popleft()
            for i2, j2 in _get_near(i1, j1):
                if matrix[i2][j2] >= matrix[i1][j1] and (i2, j2) not in visited1:
                    visited1.add((i2, j2))
                    queue1.append((i2, j2))

        # 标记大西洋
        while queue2:
            i1, j1 = queue2.popleft()
            for i2, j2 in _get_near(i1, j1):
                if matrix[i2][j2] >= matrix[i1][j1] and (i2, j2) not in visited2:
                    visited2.add((i2, j2))
                    queue2.append((i2, j2))

        # 生成结果
        return [[i, j] for (i, j) in (visited1 & visited2)]
```

