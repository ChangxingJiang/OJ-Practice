# LeetCode题解(0641)：设计循环双端队列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-circular-deque/)（中等）

标签：队列、设计

| 解法           | 时间复杂度        | 空间复杂度 | 执行用时      |
| -------------- | ----------------- | ---------- | ------------- |
| Ans 1 (Python) | 所有操作 = $O(1)$ | $O(K)$     | 84ms (84.83%) |
| Ans 2 (Python) |                   |            |               |
| Ans 3 (Python) |                   |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.index = 0
        self.count = 0
        self.size = k

    def insertFront(self, value: int) -> bool:
        if self.count < self.size:
            idx = (self.size + self.index - 1) % self.size
            self.queue[idx] = value
            self.index = idx
            self.count += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.count < self.size:
            idx = (self.index + self.count) % self.size
            self.queue[idx] = value
            self.count += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.count > 0:
            self.index = (self.index + 1) % self.size
            self.count -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.count > 0:
            self.count -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.count > 0:
            return self.queue[self.index]
        else:
            return -1

    def getRear(self) -> int:
        if self.count > 0:
            idx = (self.index + self.count - 1) % self.size
            return self.queue[idx]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
```