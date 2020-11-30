# LeetCode题解(面试16.13)：平分正方形(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bisect-squares-lcci/)（中等）

标签：几何、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 32ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        # 需要穿过两个正方形的中点
        r1, r2 = square1[2] / 2, square2[2] / 2
        x1, y1 = square1[0] + r1, square1[1] + r1
        x2, y2 = square2[0] + r2, square2[1] + r2

        # 处理中心点重叠/在与X轴垂直的直线上的情况
        if x1 == x2:
            return [x1, min(y1 - r1, y2 - r2), x1, max(y1 + r1, y2 + r2)]

        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1

        # 处理中心点在与Y轴垂直的直线上的情况
        if k == 0:
            return [min(x1 - r1, x2 - r2), b, max(x1 + r1, x2 + r2), b]

        ans = []

        # 遍历所有可能的顶点（直线与每一条边的交点）
        a1, b1, c1, d1 = [x1 - r1, x1 + r1, y1 - r1, y1 + r1]
        a2, b2, c2, d2 = [x2 - r2, x2 + r2, y2 - r2, y2 + r2]
        if c1 <= (yy := k * a1 + b) <= d1:
            ans.append([a1, yy])
        if c1 <= (yy := k * b1 + b) <= d1:
            ans.append([b1, yy])
        if c2 <= (yy := k * a2 + b) <= d2:
            ans.append([a2, yy])
        if c2 <= (yy := k * b2 + b) <= d2:
            ans.append([b2, yy])
        if a1 <= (xx := (c1 - b) / k) <= b1:
            ans.append([xx, c1])
        if a1 <= (xx := (d1 - b) / k) <= b1:
            ans.append([xx, d1])
        if a2 <= (xx := (c2 - b) / k) <= b2:
            ans.append([xx, c2])
        if a2 <= (xx := (d2 - b) / k) <= b2:
            ans.append([xx, d2])

        ans.sort()

        return ans[0] + ans[-1]
```