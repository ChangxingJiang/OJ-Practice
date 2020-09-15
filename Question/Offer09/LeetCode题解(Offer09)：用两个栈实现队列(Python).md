# LeetCode题解(Offer09)：用两个栈实现队列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)（简单）

标签：栈、设计、队列

| 解法           | 时间复杂度                                | 空间复杂度 | 执行用时        |
| -------------- | ----------------------------------------- | ---------- | --------------- |
| Ans 1 (Python) | appendTail = $O(1)$ ; deleteHead = $O(N)$ | $O(N)$     | 超出时间限制    |
| Ans 2 (Python) | appendTail = $O(1)$ ; deleteHead = $O(1)$ | $O(N)$     | 1528ms (14.36%) |
| Ans 3 (Python) | appendTail = $O(1)$ ; deleteHead = $O(1)$ | $O(N)$     | 552ms (80.79%)  |

解法一（暴力解法）：

```python
from queue import LifoQueue

class CQueue:
    def __init__(self):
        self.stack = LifoQueue()

    def appendTail(self, value: int) -> None:
        self.stack.put(value)

    def deleteHead(self) -> int:
        if self._is_empty():
            return -1
        else:
            temp = LifoQueue()
            while self.stack.qsize():
                temp.put(self.stack.get())

            ans = temp.get()
            while temp.qsize():
                self.stack.put(temp.get())

            return ans

    def _is_empty(self):
        return self.stack.qsize() == 0
```

解法二（双栈实现）：

```python
from queue import LifoQueue

class CQueue:
    def __init__(self):
        self.stack1 = LifoQueue()
        self.stack2 = LifoQueue()

    def appendTail(self, value: int) -> None:
        self.stack1.put(value)

    def deleteHead(self) -> int:
        if self.stack2.qsize() == 0:
            while self.stack1.qsize():
                self.stack2.put(self.stack1.get())
        return self.stack2.get() if self.stack2.qsize() else -1
```

解法三（Python列表的双栈实现）：

```python
class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else -1
```