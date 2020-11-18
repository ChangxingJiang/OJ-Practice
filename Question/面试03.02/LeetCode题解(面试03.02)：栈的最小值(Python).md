# LeetCode题解(面试03.02)：设计能够在常数时间内检索到最小元素的栈(Python)

题目：[原题链接](https://leetcode-cn.com/problems/min-stack-lcci/)（简单）

标签：设计、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 68ms (94.18%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.stack.append(x)
        else:
            min_val = self.stack[-1]
            self.stack.append(x)
            self.stack.append(min(min_val, x))

    def pop(self) -> None:
        self.stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-2]

    def getMin(self) -> int:
        return self.stack[-1]
```