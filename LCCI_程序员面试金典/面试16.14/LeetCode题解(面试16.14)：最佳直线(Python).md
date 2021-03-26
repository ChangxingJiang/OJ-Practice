# LeetCode题解(面试16.14)：最佳直线(Python)

题目：[原题链接](https://leetcode-cn.com/problems/best-line-lcci/)（中等）

标签：哈希表、几何

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 超出时间限制   |
| Ans 2 (Python) | $O(N^2)$   | $O(N^2)$   | 408ms (57.48%) |
| Ans 3 (Python) |            |            |                |

解法一：

```python
from fractions import Fraction

class Solution:

    def bestLine(self, points: List[List[int]]) -> List[int]:
        if len(points) <= 1:
            return []

        point_dic = collections.defaultdict(set)
        for i, point in enumerate(points):
            point_dic[(point[0], point[1])].add(i)

        count_line = collections.defaultdict(set)

        # 生成所有直线
        # O(N^2)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 != x2 or y1 != y2:
                    k = Fraction((y2 - y1), (x2 - x1)) if x1 != x2 else float("inf")
                    b = y1 - x1 * k if k != float("inf") else x1  # 如果斜率为正无穷，则截距记录竖线的x坐标
                    count_line[(k, b)] |= point_dic[(x1, y1)]
                    count_line[(k, b)] |= point_dic[(x2, y2)]

        # print(count_line)

        # 提取最高频率的直线
        line = [list(sorted(n)) for n in count_line.values()]
        line.sort(key=lambda x: (-len(x), x[0], x[1]))
        return line[0][:2]
```

解法二（不使用Franction模块处理相近的小数）：

```python
class Solution:

    def bestLine(self, points: List[List[int]]) -> List[int]:

        count_line = collections.defaultdict(set)

        # 生成所有直线
        # O(N^2)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 != x2 or y1 != y2:
                    k = (y2 - y1)/ (x2 - x1) if x1 != x2 else float("inf")
                    b = y1 - x1 * k if k != float("inf") else x1  # 如果斜率为正无穷，则截距记录竖线的x坐标
                    count_line[(k, b)].add(i)
                    count_line[(k, b)].add(j)

        # print(count_line)

        # 提取最高频率的直线
        line = [list(sorted(n)) for n in count_line.values()]
        line.sort(key=lambda x: (-len(x), x[0], x[1]))
        return line[0][:2]
```





