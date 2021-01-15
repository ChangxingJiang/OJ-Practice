# LeetCode题解(0427)：建立四叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/construct-quad-tree/)（中等）

标签：递归、分治算法、树

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时       |
| -------------- | ------------ | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2logN)$ | $O(N^2)$   | 116ms (85.57%) |
| Ans 2 (Python) |              |            |                |
| Ans 3 (Python) |              |            |                |

解法一（暴力解法）：

```python
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        s = sum(map(sum, grid))
        m = len(grid) >> 1
        if not s or not m or s == 4 * m * m:
            return Node(bool(s), True, None, None, None, None)
        else:
            return Node(True, False,
                        self.construct([g[: m] for g in grid[: m]]),
                        self.construct([g[m:] for g in grid[: m]]),
                        self.construct([g[: m] for g in grid[m:]]),
                        self.construct([g[m:] for g in grid[m:]]))
```

