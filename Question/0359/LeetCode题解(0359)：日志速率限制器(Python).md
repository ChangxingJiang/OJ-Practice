# LeetCode题解(0359)：日志速率限制器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/logger-rate-limiter/)（简单）

标签：设计、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(1)$     | $O(N)$     | 160ms (93.50%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Logger:

    def __init__(self):
        self.log = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.log or timestamp - self.log[message] >= 10:
            self.log[message] = timestamp
            return True
        else:
            return False
```