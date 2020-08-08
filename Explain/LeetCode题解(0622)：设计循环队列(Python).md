# LeetCode题解(0622)：设计循环队列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-circular-queue/)（中等）

标签：队列

| 解法           | 时间复杂度        | 空间复杂度 | 执行用时      |
| -------------- | ----------------- | ---------- | ------------- |
| Ans 1 (Python) | 所有操作 = $O(1)$ | $O(K)$     | 80ms (89.72%) |
| Ans 2 (Python) |                   |            |               |
| Ans 3 (Python) |                   |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用定长列表实现）：

```python
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0] * k
        self.index = 0
        self.count = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count < self.size:
            self.queue[(self.index + self.count) % self.size] = value
            self.count += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count > 0:
            self.index = (self.index + 1) % self.size
            self.count -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count > 0:
            return self.queue[self.index]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.count > 0:
            return self.queue[(self.index + self.count - 1) % self.size]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.size
```