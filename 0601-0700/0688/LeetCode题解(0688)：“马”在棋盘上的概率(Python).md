# LeetCode题解(0688)：“马”在棋盘上的概率(Python)

题目：[原题链接](https://leetcode-cn.com/problems/knight-probability-in-chessboard/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2×K)$ | $O(N^2)$   | 168ms (73.86%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def knightProbability(self, n: int, k: int, r: int, c: int) -> float:
        def get_next(x1, y1):
            res = []
            for (x2, y2) in [(x1 - 2, y1 - 1), (x1 - 2, y1 + 1), (x1 - 1, y1 + 2), (x1 + 1, y1 + 2),
                             (x1 + 2, y1 + 1), (x1 + 2, y1 - 1), (x1 + 1, y1 - 2), (x1 - 1, y1 - 2)]:
                if 0 <= x2 < n and 0 <= y2 < n:
                    res.append((x2, y2))
            return res

        now = [[0] * n for _ in range(n)]
        now[r][c] = 1
        for _ in range(k):
            next = [[0] * n for _ in range(n)]
            for i1 in range(n):
                for j1 in range(n):
                    if now[i1][j1]:
                        for (i2, j2) in get_next(i1, j1):
                            next[i2][j2] += now[i1][j1]
            now = next

        return sum(sum(row) for row in now) / 8 ** k
```

