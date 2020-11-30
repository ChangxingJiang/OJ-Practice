# LeetCode题解(0149)：直线上最多的点数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-points-on-a-line/)（困难）

标签：哈希表、数学、几何

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 2220ms (5.15%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
from fractions import Fraction


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1

        count_line = collections.Counter()
        count_point = collections.Counter()

        # 生成所有直线
        # O(N^2)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    count_point[(x1, y1)] += 1
                else:
                    # k = (y2 - y1) / (x2 - x1) if x1 != x2 else float("inf")
                    k = Fraction((y2 - y1), (x2 - x1)) if x1 != x2 else float("inf")
                    b = y1 - x1 * k if k != float("inf") else x1  # 如果斜率为正无穷，则截距记录竖线的x坐标
                    # print((x1, y1), (x2, y2), "->", (k, b))
                    count_line[(k, b)] += 1

        if not count_line:
            return len(points)

        # 提取最高频率的直线
        (k, b), v = count_line.most_common(1)[0]
        # print("T1:", k, b, v)

        # 处理重叠的点的情况
        # O(N)
        for (x, y), n in count_point.items():
            if y == k * x + b:
                v += n
        # 此时的v是(1+ans)*ans/2的结果

        # print("T2:", k, b, v)

        # 计算实际结果
        return math.ceil(math.sqrt(v * 2))
```