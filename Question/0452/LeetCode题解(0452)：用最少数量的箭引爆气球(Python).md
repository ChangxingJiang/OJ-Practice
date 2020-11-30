# LeetCode题解(0452)：用最少数量的箭引爆气球(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/)（中等）

标签：贪心算法、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 80ms (97.90%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        now = points[0][1]
        ans = 0

        for i1, i2 in points:
            if i1 > now:
                now = i2
                ans += 1

        return ans + 1
```