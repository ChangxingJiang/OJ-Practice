# LeetCode题解(0807)：保持城市天际线(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 76ms (93.28%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = [0] * m, [0] * n

        for i in range(m):
            for j in range(n):
                rows[i] = max(rows[i], grid[i][j])
                cols[j] = max(cols[j], grid[i][j])

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += min(rows[i], cols[j]) - grid[i][j]
        return ans
```

