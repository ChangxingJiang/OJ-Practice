# LeetCode题解(Offer30)：设计能够在常数时间内检索到最小元素的栈(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/)（简单）

标签：栈、设计

| 解法           | 时间复杂度                                                   | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | push = $O(1)$ ; pop = $O(N)$ ; top = $O(1)$ ; getMin = $O(1)$ | $O(N)$     | 72ms (92.58%) |
| Ans 2 (Python) |                                                              |            |               |
| Ans 3 (Python) |                                                              |            |               |

解法一：

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min_val is None or x < self.min_val:
            self.min_val = x

    def pop(self) -> None:
        ans = self.stack.pop()
        if ans == self.min_val:
            if self.stack:
                self.min_val = min(self.stack)
            else:
                self.min_val = None

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_val
```