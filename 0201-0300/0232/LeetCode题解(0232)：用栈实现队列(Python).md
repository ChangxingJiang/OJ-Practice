# LeetCode题解(0232)：用栈实现队列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/implement-queue-using-stacks/)（简单）

标签：栈、队列、设计

相关题目：0225（用队列实现栈）

| 解法           | 时间复杂度                                                   | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | push = $O(1)$ ; pop = $O(N)$ ; peek= $O(N)$ ; empty = $O(1)$ | $O(N)$     | 40ms (63.47%) |
| Ans 2 (Python) | push = $O(1)$ ; pop = $O(1)$ ; peek= $O(1)$ ; empty = $O(1)$ | $O(N)$     | 36ms (84.25%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用queue的栈实现，符合题目要求）：

```python
from queue import LifoQueue


class MyQueue:

    def __init__(self):
        self.stark = LifoQueue()

    def push(self, x: int) -> None:
        self.stark.put(x)

    def pop(self) -> int:
        temp = LifoQueue()
        for _ in range(self.stark.qsize() - 1):
            temp.put(self.stark.get())

        ans = self.stark.get()

        for _ in range(temp.qsize()):
            self.stark.put(temp.get())
        return ans

    def peek(self) -> int:
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
        return self.stark.qsize() == 0
```

解法二（使用Python列表实现，不符合题目要求）：

```python
class MyQueue:

    def __init__(self):
        self.stark = []

    def push(self, x: int) -> None:
        self.stark.append(x)

    def pop(self) -> int:
        return self.stark.pop(0)

    def peek(self) -> int:
        return self.stark[0]

    def empty(self) -> bool:
        return len(self.stark) == 0
```