# LeetCode题解(0478)：在圆内随机生成点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/generate-random-point-in-a-circle/)（中等）

标签：随机、拒绝采样、数学

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时       |
| -------------- | ------------- | ---------- | -------------- |
| Ans 1 (Python) | 期望 : $O(1)$ | $O(1)$     | 168ms (65.61%) |
| Ans 2 (Python) |               |            |                |
| Ans 3 (Python) |               |            |                |

解法一：

```python
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius, self.x_center, self.y_center = radius, x_center, y_center
        self.x_min, self.x_max = self.x_center - self.radius, self.x_center + self.radius
        self.y_min, self.y_max = self.y_center - self.radius, self.y_center + self.radius

    def randPoint(self) -> List[float]:
        x, y = 0, 0
        distance = float("inf")
        while distance > self.radius:
            x, y = random.uniform(self.x_min, self.x_max), random.uniform(self.y_min, self.y_max)
            distance = pow(pow((x - self.x_center), 2) + pow((y - self.y_center), 2), 0.5)
        return [x, y]
```