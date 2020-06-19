# LeetCode题解(0232)：用栈实现队列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/implement-queue-using-stacks/)（简单）

与题目0225配套，互为相反。

| 解法           | 执行用时       |
| -------------- | -------------- |
| Ans 1 (Python) | 40ms (>63.47%) |
| Ans 2 (Python) | 36ms (>84.25%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用queue的栈实现）：

```python
from queue import LifoQueue


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stark = LifoQueue()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stark.put(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        temp = LifoQueue()
        for _ in range(self.stark.qsize() - 1):
            temp.put(self.stark.get())

        ans = self.stark.get()

        for _ in range(temp.qsize()):
            self.stark.put(temp.get())
        return ans

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stark.qsize() != 0:
            temp = LifoQueue()
            for _ in range(self.stark.qsize() - 1):
                temp.put(self.stark.get())

            ans = self.stark.get()

            self.stark.put(ans)
            for _ in range(temp.qsize()):
                self.stark.put(temp.get())

            return ans

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stark.qsize() == 0
```

解法二（使用Python列表实现，不符合题目要求）：

```python
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stark = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stark.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stark.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stark[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stark) == 0
```