# LeetCode题解(0716)：最大栈(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-stack/)（简单）

标签：设计、栈

| 解法           | 时间复杂度                                      | 空间复杂度 | 执行用时       |
| -------------- | ----------------------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | push,pop,top,peekMax = $O(1)$ ; popMax = $O(N)$ | $O(N)$     | 160ms (87.91%) |
| Ans 2 (Python) |                                                 |            |                |
| Ans 3 (Python) |                                                 |            |                |

解法一：

```python
class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = [-10000001]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.max_stack.append(max(x, self.max_stack[-1]))

    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        val = self.max_stack.pop()

        temp = [self.stack.pop()]
        while temp[-1] != val:
            self.max_stack.pop()
            temp.append(self.stack.pop())

        temp.pop()

        while temp:
            v = temp.pop()
            self.stack.append(v)
            self.max_stack.append(max(v, self.max_stack[-1]))

        return val
```