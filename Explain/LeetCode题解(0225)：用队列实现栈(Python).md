# LeetCode题解(0225)：用队列实现栈(Python)

题目：[原题链接](https://leetcode-cn.com/problems/implement-stack-using-queues/)（简单）

| 解法           | 执行用时       |
| -------------- | -------------- |
| Ans 1 (Python) | 28ms (>98.79%) |
| Ans 2 (Python) | 32ms (>95.10%) |
| Ans 3 (Python) | 40ms (>64.03%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（不使用队列实现）：

```python
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.size -= 1
        return self.stack.pop(self.size - 1)

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.size == 0:
            return None
        else:
            return self.stack[self.size - 1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0
```

解法二（使用queue的LifoQueue实现）：

LifoQueue = Last In First Our Queue（栈）

```python
from queue import LifoQueue


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = LifoQueue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        x = self.queue.get()
        self.push(x)
        return x

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue.empty()
```

解法三（使用Queue的队列实现栈）：

```python
from queue import Queue


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.put(x)
        for _ in range(self.queue.qsize() - 1):  # 将栈顶元素移动到队头位置
            self.queue.put(self.queue.get())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        ans = self.queue.get()
        self.push(ans)
        return ans

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue.empty()
```