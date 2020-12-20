# LeetCode题解(0362)：敲击计数器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-hit-counter/)（中等）

标签：设计、队列

| 解法           | 时间复杂度 | 空间复杂度                    | 执行用时      |
| -------------- | ---------- | ----------------------------- | ------------- |
| Ans 1 (Python) | $O(1*)$    | $O(N)$ : N为5分钟内的敲击次数 | 40ms (62.67%) |
| Ans 2 (Python) |            |                               |               |
| Ans 3 (Python) |            |                               |               |

解法一：

```python
class HitCounter:

    def __init__(self):
        self.queue = collections.deque()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()
        return len(self.queue)
```