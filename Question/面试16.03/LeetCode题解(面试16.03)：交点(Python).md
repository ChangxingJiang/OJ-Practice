# LeetCode题解(面试16.03)：交点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/intersection-lcci/)（困难）

标签：几何、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 44ms (38.46%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        k1 = (end1[1] - start1[1]) / (end1[0] - start1[0]) if end1[0] != start1[0] else float("inf")
        k2 = (end2[1] - start2[1]) / (end2[0] - start2[0]) if end2[0] != start2[0] else float("inf")

        # 处理两条线段均垂直于X轴的情况
        if k1 == k2 == float("inf"):
            if (start1[0] != start2[0]
                    or min(start1[1], end1[1]) > max(start2[1], end2[1])
                    or max(start1[1], end1[1]) < min(start2[1], end2[1])):
                return []
            return [start1[0], max(start1[1], start2[1])]

        b1 = start1[1] - k1 * start1[0] if k1 != float("inf") else start1[0]
        b2 = start2[1] - k2 * start2[0] if k2 != float("inf") else start2[0]

        # 处理两条线段为平行线的情况
        if k1 == k2:
            if (b1 != b2
                    or min(start1[1], end1[1]) > max(start2[1], end2[1])
                    or max(start1[1], end1[1]) < min(start2[1], end2[1])):
                return []
            return [max(start1[0], start2[0]), max(start1[1], start2[1])]

        # 处理有一条线段平行与X轴的情况
        if k1 == float("inf"):
            k1, k2, b1, b2 = k2, k1, b2, b1
        if k2 == float("inf"):
            x = b2
            y = k1 * x + b1
            if (min(start1[1], end1[1]) <= y <= max(start1[1], end1[1])
                    and min(start2[1], end2[1]) <= y <= max(start2[1], end2[1])):
                return [x, y]
            else:
                return []

        # 计算两条线段的交点
        x = (b1 - b2) / (k2 - k1)
        y = k1 * x + b1

        if (not min(start1[0], end1[0]) <= x <= max(start1[0], end1[0])
                or not min(start1[1], end1[1]) <= y <= max(start1[1], end1[1])
                or not min(start2[0], end2[0]) <= x <= max(start2[0], end2[0])
                or not min(start2[1], end2[1]) <= y <= max(start2[1], end2[1])):
            return []

        return [x, y]
```