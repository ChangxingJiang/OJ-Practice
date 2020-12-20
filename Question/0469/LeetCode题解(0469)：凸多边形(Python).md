# LeetCode题解(0469)：凸多边形(Python)

题目：[原题链接](https://leetcode-cn.com/problems/convex-polygon/)（中等）

标签：几何、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 232ms (62.96%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        size = len(points)
        pre = 0
        for i in range(size):
            x1 = points[(i + 1) % size][0] - points[i][0]
            x2 = points[(i + 2) % size][0] - points[i][0]
            y1 = points[(i + 1) % size][1] - points[i][1]
            y2 = points[(i + 2) % size][1] - points[i][1]
            cur = x1 * y2 - x2 * y1
            if cur != 0:
                if cur * pre < 0:
                    return False
                else:
                    pre = cur
        return True
```