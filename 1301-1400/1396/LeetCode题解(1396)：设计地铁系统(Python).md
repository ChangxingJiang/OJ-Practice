# LeetCode题解(1396)：设计地铁系统(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-underground-system/)（中等）

标签：设计

| 解法           | 时间复杂度                                                   | 空间复杂度 | 执行用时       |
| -------------- | ------------------------------------------------------------ | ---------- | -------------- |
| Ans 1 (Python) | checkIn = $O(1)$ ; checkOut = $O(1)$ ; getAverageTime = $O(1)$ | $O(S+P)$   | 200ms (85.40%) |
| Ans 2 (Python) |                                                              |            |                |
| Ans 3 (Python) |                                                              |            |                |

解法一：

```python
class UndergroundSystem:

    def __init__(self):
        self.time_info = {}
        self.passenger = {}

    def checkIn(self, id: int, station1: str, t1: int) -> None:
        self.passenger[id] = [station1, t1]

    def checkOut(self, id: int, station2: str, t2: int) -> None:
        station1, t1 = self.passenger[id]
        if (station1, station2) not in self.time_info:
            self.time_info[(station1, station2)] = [0, 0]
        self.time_info[(station1, station2)][0] += t2 - t1
        self.time_info[(station1, station2)][1] += 1

    def getAverageTime(self, station1: str, station2: str) -> float:
        return self.time_info[(station1, station2)][0] / self.time_info[(station1, station2)][1]
```

