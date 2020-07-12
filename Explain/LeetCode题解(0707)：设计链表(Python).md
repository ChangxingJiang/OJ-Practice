# LeetCode题解(0707)：设计链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-linked-list/)（中等）

标签：链表、设计

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | --         | 208ms (77.36%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
class MyLinkedList:
    class _Node:
        """"""
        __slots__ = "value", "next"

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return str(self.value) + "->" + str(self.next)

    def __init__(self):
        self._head = self._Node(0)
        self._size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self._size:
            return -1
        curr = self._head
        for _ in range(index + 1):
            curr = curr.next
        return curr.value

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self._size:
            return
        self._size += 1
        prev = self._head
        for _ in range(index):
            prev = prev.next
        node = self._Node(val, prev.next)
        prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self._size:
            return

        self._size -= 1
        prev = self._head
        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next
```