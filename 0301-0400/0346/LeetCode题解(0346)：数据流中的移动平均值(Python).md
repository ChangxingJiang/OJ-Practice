# LeetCode题解(0346)：数据流中的移动平均值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/moving-average-from-data-stream/)（简单）

标签：设计、队列

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 76ms (92.89%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class MovingAverage:

    def __init__(self, size: int):
        self.array = deque()
        self.total = 0
        self.size = size

    def next(self, val: int) -> float:
        if len(self.array) == self.size:
            self.total -= self.array.popleft()

        self.array.append(val)
        self.total += val
        return self.total / len(self.array)
```