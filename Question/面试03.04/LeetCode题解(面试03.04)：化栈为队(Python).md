# LeetCode题解(面试03.04)：用两个栈实现队列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci/)（简单）

标签：设计、栈、队列

| 解法           | 时间复杂度                        | 空间复杂度 | 执行用时      |
| -------------- | --------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | POP/PEEK = $O(1)$ ; PUSH = $O(N)$ | $O(N)$     | 32ms (95.65%) |
| Ans 2 (Python) |                                   |            |               |
| Ans 3 (Python) |                                   |            |               |

解法一：

```python
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(x)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        if self.empty():
            return -1
        else:
            return self.stack1.pop()

    def peek(self) -> int:
        if self.empty():
            return -1
        else:
            return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0
```