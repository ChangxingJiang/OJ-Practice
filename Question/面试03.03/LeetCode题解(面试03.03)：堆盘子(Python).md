# LeetCode题解(面试03.03)：堆盘子(Python)

题目：[原题链接](https://leetcode-cn.com/problems/stack-of-plates-lcci/)（中等）

标签：设计、栈

| 解法           | 时间复杂度                         | 空间复杂度 | 执行用时       |
| -------------- | ---------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | PUSH/POP = $O(1)$ ; POPAT = $O(N)$ | $O(N)$     | 120ms (98.53%) |
| Ans 2 (Python) |                                    |            |                |
| Ans 3 (Python) |                                    |            |                |

解法一：

```python
class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.stacks = []

    def push(self, val: int) -> None:
        if self.cap > 0:
            if self.stacks and len(self.stacks[-1]) < self.cap:
                self.stacks[-1].append(val)
            else:
                self.stacks.append([val])

    def pop(self) -> int:
        if not self.stacks:
            return -1

        val = self.stacks[-1].pop()

        if not self.stacks[-1]:
            self.stacks.pop()

        return val

    def popAt(self, index: int) -> int:
        if index >= len(self.stacks):
            return -1

        val = self.stacks[index].pop()

        if not self.stacks[index]:
            self.stacks.pop(index)

        return val
```