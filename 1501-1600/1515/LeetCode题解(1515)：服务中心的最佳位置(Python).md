# LeetCode题解(1515)：服务中心的最佳位置(Python)

题目：[原题链接](https://leetcode-cn.com/problems/best-position-for-a-service-centre/)（困难）

标签：几何、数学、机器学习

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时       |
| -------------- | ------------ | ---------- | -------------- |
| Ans 1 (Python) | $O(Nlog^2N)$ | $O(N)$     | 5444ms (5.33%) |
| Ans 2 (Python) |              |            |                |
| Ans 3 (Python) |              |            |                |

解法一：

```python
class Solution:
    _MOD = 1e-7

    def __init__(self):
        self.positions = []

    def get_distance(self, cx, cy):
        return sum(((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 for x, y in self.positions)

    def getMinDistSum(self, positions: List[List[int]]) -> float:
        self.positions = positions

        x_left, x_right = 0, 100
        while x_right - x_left > self._MOD:
            x_first = (x_left + x_left + x_right) / 3
            x_second = (x_left + x_right + x_right) / 3
            if self.count_y(x_first) < self.count_y(x_second):
                x_right = x_second
            else:
                x_left = x_first

        return self.count_y(x_left)

    def count_y(self, x_center):
        y_left, y_right = 0, 100
        while y_right - y_left > self._MOD:
            y_first = (y_left + y_left + y_right) / 3
            y_second = (y_left + y_right + y_right) / 3
            if self.get_distance(x_center, y_first) < self.get_distance(x_center, y_second):
                y_right = y_second
            else:
                y_left = y_first
        return self.get_distance(x_center, y_left)
```