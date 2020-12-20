# LeetCode题解(0963)：最小面积矩形II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-area-rectangle-ii/)（中等）

标签：几何、数学

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时      |
| -------------- | ------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2logN)$ | $O(N^2)$   | 92ms (92.68%) |
| Ans 2 (Python) |              |            |               |
| Ans 3 (Python) |              |            |               |

解法一：

```python
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # 不是3组长度相等的边就是矩形的经典反例：[3, 0] [1, 0] [2, 3] [2, 1]

        # 构造复数用于计算
        points = [complex(*point) for point in points]
        dic = collections.defaultdict(list)

        for p1, p2 in itertools.combinations(points, 2):
            center = (p1 + p2) / 2
            radius = abs(center - p1)
            dic[(center, radius)].append(p1)

        ans = float("inf")

        for (center, radius), candidates in dic.items():
            for p1, p2 in itertools.combinations(candidates, 2):
                ans = min(ans, abs(p1 - p2) * abs(p1 - (2 * center - p2)))

        return ans if ans != float("inf") else 0
```