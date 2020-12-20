# LeetCode题解(1453)：圆形靶内的最大飞镖数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/)（困难）

标签：几何、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(1)$     | 1356ms (45.28%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def __init__(self):
        self.points = []
        self.r = 0

    def numPoints(self, points: List[List[int]], r: int) -> int:
        self.points = points
        self.r = r

        size = len(self.points)

        ans = 1
        for i in range(size):
            for j in range(i + 1, size):
                x1, y1 = points[i]
                x2, y2 = points[j]

                # 计算两个点之间的距离
                d = (x2 - x1) ** 2 + (y1 - y2) ** 2

                # 如果两个点之间的距离超过直径，则两个点无法在一个圆上
                if d > ((2 * r) ** 2):
                    continue

                # 计算以这两个点在圆上的圆心坐标（有两个解）
                px = (x1 + x2) / 2
                py = (y1 + y2) / 2
                dx = x2 - x1
                dy = y2 - y1
                h = math.sqrt(r ** 2 - d / 4)

                cx1 = h * dy / math.sqrt(dx ** 2 + dy ** 2) + px
                cy1 = -h * dx / math.sqrt(dx ** 2 + dy ** 2) + py
                cx2 = -h * dy / math.sqrt(dx ** 2 + dy ** 2) + px
                cy2 = h * dx / math.sqrt(dx ** 2 + dy ** 2) + py
                ans = max(ans, self.count_inside_num(cx1, cy1), self.count_inside_num(cx2, cy2))

        return ans

    def count_inside_num(self, cx, cy):
        ans = 0
        for x, y in self.points:
            if (x - cx) ** 2 + (y - cy) ** 2 <= self.r ** 2:
                ans += 1
        return ans
```