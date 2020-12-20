# LeetCode题解(1401)：圆和矩形是否有重叠(Python)

题目：[原题链接](https://leetcode-cn.com/problems/circle-and-rectangle-overlapping/)（中等）

标签：几何、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 44ms (37.96%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def distance(x, y):
            return math.sqrt(math.pow(y[1] - x[1], 2) + math.pow(y[0] - x[0], 2))

        # 检查圆心是否在矩形内
        if x1 <= x_center <= x2 and y1 <= y_center <= y2:
            return True

        # 检查圆的边缘是否相交
        if x_center > x2 and y1 <= y_center <= y2:
            return x_center - x2 <= radius
        if x_center < x1 and y1 <= y_center <= y2:
            return x1 - x_center <= radius
        if y_center > y2 and x1 <= x_center <= x2:
            return y_center - y2 <= radius
        if y_center < y1 and x1 <= x_center <= x2:
            return y1 - y_center <= radius

        # 检查矩形的四个顶点是否在圆内
        elif (distance((x_center, y_center), (x1, y1)) <= radius or
              distance((x_center, y_center), (x1, y2)) <= radius or
              distance((x_center, y_center), (x2, y1)) <= radius or
              distance((x_center, y_center), (x2, y2)) <= radius):
            return True

        return False
```