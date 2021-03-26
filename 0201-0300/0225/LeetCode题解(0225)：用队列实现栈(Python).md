# LeetCode题解(0225)：用队列实现栈(Python)

题目：[原题链接](https://leetcode-cn.com/problems/implement-stack-using-queues/)（简单）

标签：栈、队列、设计

| 解法           | 时间复杂度                                                   | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | push = $O(1)$ ; pop = $O(1)$ ; top = $O(1)$ ; empty = $O(1)$ | $O(N)$     | 28ms (98.79%) |
| Ans 2 (Python) | push = $O(1)$ ; pop = $O(1)$ ; top = $O(1)$ ; empty = $O(1)$ | $O(N)$     | 32ms (95.10%) |
| Ans 3 (Python) | push = $O(N)$ ; pop = $O(1)$ ; top = $O(N)$ ; empty = $O(1)$ | $O(N)$     | 36ms (85.84%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用列表实现，不符合题目要求）：

```python
class MyStack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.stack.pop(self.size - 1)

    def top(self) -> int:
        if self.size == 0:
            return None
        else:
            return self.stack[self.size - 1]

    def empty(self) -> bool:
        return self.size == 0
```

解法二（使用queue的栈实现，不符合题目要求）：

LifoQueue = Last In First Our Queue（栈）

```python
from queue import LifoQueue


class MyStack:

    def __init__(self):
        self.queue = LifoQueue()

    def push(self, x: int) -> None:
        self.queue.put(x)

    def pop(self) -> int:
        return self.queue.get()

    def top(self) -> int:
        x = self.queue.get()
        self.push(x)
        return x

    def empty(self) -> bool:
        return self.queue.empty()
```

解法三（使用Queue的队列实现栈，符合题目要求）：

```python
from queue import Queue


class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.put(x)
        for _ in range(self.queue.qsize() - 1):  # 将栈顶元素移动到队头位置
            self.queue.put(self.queue.get())

    def pop(self) -> int:
        return self.queue.get()

    def top(self) -> int:
        ans = self.queue.get()
        self.push(ans)
        return ans

    def empty(self) -> bool:
        return self.queue.empty()
```