# LeetCode题解(1603)：设计停车系统(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-parking-system/)（简单）

标签：设计

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 160ms (81%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.big -= 1
            return self.big >= 0
        if carType == 2:
            self.medium -= 1
            return self.medium >= 0
        if carType == 3:
            self.small -= 1
            return self.small >= 0
```