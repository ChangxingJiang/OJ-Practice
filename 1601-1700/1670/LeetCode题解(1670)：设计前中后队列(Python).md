# LeetCode题解(1670)：设计前中后队列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-front-middle-back-queue/)（中等）

标签：设计、链表、队列

| 解法           | 时间复杂度             | 空间复杂度 | 执行用时      |
| -------------- | ---------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$ : 其中N为操作数 | $O(N)$     | 96ms (26.96%) |
| Ans 2 (Python) |                        |            |               |
| Ans 3 (Python) |                        |            |               |

解法一（双端队列）：

```python
class FrontMiddleBackQueue:
    class _Node:
        __slots__ = ("val", "prev", "next")

        def __init__(self, val, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

        def __str__(self):
            prev = str(self.prev.val) if self.prev else "None"
            next = str(self.next.val) if self.next else "None"
            return str(self.val) + "(" + prev + "," + next + ")" + "->" + str(self.next)

    def __init__(self):
        self.head = self._Node(0)
        self.tail = self._Node(0)
        self.head.next, self.tail.prev = self.tail, self.head

        self.middle = self.head  # 中间节点
        self.idx, self.n = -1, 0  # 中间节点坐标、数组长度

    def pushFront(self, val: int) -> None:
        prev, next = self.head, self.head.next
        node = self._Node(val, prev, next)
        prev.next, next.prev = node, node

        self.idx = self.idx + 1 if self.idx >= 0 else -1
        self.n += 1

    def pushMiddle(self, val: int) -> None:
        self._update_middle()

        if self.idx == -1:  # self.n = 0
            self.pushFront(val)
        else:
            if self.n % 2 == 0:
                prev, next = self.middle, self.middle.next
            else:
                self.idx += 1
                prev, next = self.middle.prev, self.middle
            node = self._Node(val, prev, next)
            prev.next, next.prev = node, node

            self.n += 1

    def pushBack(self, val: int) -> None:
        prev, next = self.tail.prev, self.tail
        node = self._Node(val, prev, next)
        prev.next, next.prev = node, node

        self.n += 1

    def popFront(self) -> int:
        if self.n == 0:
            return -1

        self.idx = self.idx - 1 if self.idx >= 0 else -1
        self.n -= 1
        val = self.head.next.val

        prev, next = self.head, self.head.next.next
        prev.next, next.prev = next, prev

        if self.n == 0:
            self.idx = -1
            self.head.next, self.tail.prev = self.tail, self.head

        return val

    def popMiddle(self) -> int:
        if self.n == 0:
            return -1

        self._update_middle()

        val = self.middle.val
        prev, next = self.middle.prev, self.middle.next

        if self.n % 2 == 0:
            self.middle = self.middle.next
        else:
            self.idx -= 1
            self.middle = self.middle.prev

        prev.next, next.prev = next, prev

        self.n -= 1

        if self.n == 0:
            self.idx = -1
            self.head.next, self.tail.prev = self.tail, self.head

        return val

    def popBack(self) -> int:
        if self.n == 0:
            return -1

        self.n -= 1
        val = self.tail.prev.val

        prev, next = self.tail.prev.prev, self.tail
        prev.next, next.prev = next, prev

        if self.n == 0:
            self.idx = -1
            self.head.next, self.tail.prev = self.tail, self.head

        return val

    def _update_middle(self):
        """更新中间位置：时间复杂度=O(1)(摊销)"""
        if self.idx <= -1:
            self.middle = self.head
        if self.idx >= self.n:
            self.middle = self.tail

        if self.n > 0:
            aim = (self.n - 1) // 2  # 计算正确的中间位置坐标
            while self.idx < aim:
                self.idx += 1
                self.middle = self.middle.next
            while self.idx > aim:
                self.idx -= 1
                self.middle = self.middle.prev
        else:
            self.idx = -1
```