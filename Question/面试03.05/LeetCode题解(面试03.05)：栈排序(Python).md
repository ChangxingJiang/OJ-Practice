# LeetCode题解(面试03.05)：栈排序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sort-of-stacks-lcci/)（中等）

标签：设计、栈、排序

| 解法           | 时间复杂度                        | 空间复杂度 | 执行用时       |
| -------------- | --------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | push = $O(N)$ ; pop,peek = $O(1)$ | $O(N)$     | 972ms (52.96%) |
| Ans 2 (Python) |                                   |            |                |
| Ans 3 (Python) |                                   |            |                |

解法一：

```python
class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        temp = []
        while self.stack and self.stack[-1] < val:
            temp.append(self.stack.pop())

        self.stack.append(val)

        while temp:
            self.stack.append(temp.pop())

    def pop(self) -> None:
        if not self.isEmpty():
            self.stack.pop()

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.stack[-1]

    def isEmpty(self) -> bool:
        return len(self.stack) == 0
```