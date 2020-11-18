# LeetCode题解(1631)：计算二维地图中到达目的地的最小体力消耗路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/path-with-minimum-effort/)（中等）

标签：数学、几何、图、深度优先搜索、并查集、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 1740ms (60%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        table = [[0] * col for _ in range(row)]

        for i in range(1, row):
            table[i][0] = max(table[i - 1][0], abs(heights[i][0] - heights[i - 1][0]))

        for j in range(1, col):
            table[0][j] = max(table[0][j - 1], abs(heights[0][j] - heights[0][j - 1]))

        need = collections.deque()

        for i in range(1, row):
            for j in range(1, col):
                table[i][j] = min(
                    max(table[i - 1][j], abs(heights[i][j] - heights[i - 1][j])),
                    max(table[i][j - 1], abs(heights[i][j] - heights[i][j - 1]))
                )
                if max(table[i][j], abs(heights[i][j] - heights[i - 1][j])) < table[i - 1][j]:
                    table[i - 1][j] = max(table[i][j], abs(heights[i][j] - heights[i - 1][j]))
                    need.append((i - 1, j))
                if max(table[i][j], abs(heights[i][j] - heights[i][j - 1])) < table[i][j - 1]:
                    table[i][j - 1] = max(table[i][j], abs(heights[i][j] - heights[i][j - 1]))
                    need.append((i, j - 1))

        while need:
            i, j = need.popleft()
            if i > 0 and max(table[i][j], abs(heights[i][j] - heights[i - 1][j])) < table[i - 1][j]:
                table[i - 1][j] = max(table[i][j], abs(heights[i][j] - heights[i - 1][j]))
                need.append((i - 1, j))
            if i < row - 1 and max(table[i][j], abs(heights[i][j] - heights[i + 1][j])) < table[i + 1][j]:
                table[i + 1][j] = max(table[i][j], abs(heights[i][j] - heights[i + 1][j]))
                need.append((i + 1, j))
            if j > 0 and max(table[i][j], abs(heights[i][j] - heights[i][j - 1])) < table[i][j - 1]:
                table[i][j - 1] = max(table[i][j], abs(heights[i][j] - heights[i][j - 1]))
                need.append((i, j - 1))
            if j < col - 1 and max(table[i][j], abs(heights[i][j] - heights[i][j + 1])) < table[i][j + 1]:
                table[i][j + 1] = max(table[i][j], abs(heights[i][j] - heights[i][j + 1]))
                need.append((i, j + 1))

        return table[-1][-1]
```