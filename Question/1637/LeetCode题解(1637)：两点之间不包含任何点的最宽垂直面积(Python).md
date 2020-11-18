# LeetCode题解(1637)：两点之间不包含任何点的最宽垂直面积(Python)

题目：[原题链接](https://leetcode-cn.com/problems/widest-vertical-area-between-two-points-containing-no-points/)（中等）

标签：数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 296ms (10%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()

        ans = 0
        last = -1
        for point in points:
            if last == -1:
                last = point[0]
            else:
                ans = max(ans, point[0] - last)
                last = point[0]

        return ans
```

