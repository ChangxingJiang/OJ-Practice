# LeetCode题解(1779)：找到最近的有相同X或Y坐标的点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(P)$     | $O(1)$     | 84ms (90.07%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def nearestValidPoint(self, x1: int, y1: int, points: List[List[int]]) -> int:
        min_distance = float("inf")
        ans = -1
        for i in range(len(points)):
            x2, y2 = points[i]
            if x1 == x2 or y1 == y2:
                distance = abs(x1 - x2) + abs(y1 - y2)
                if distance < min_distance:
                    min_distance = distance
                    ans = i
        return ans
```

