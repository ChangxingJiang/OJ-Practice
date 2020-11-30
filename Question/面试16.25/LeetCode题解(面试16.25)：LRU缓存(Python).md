# LeetCode题解(面试16.25)：LRU缓存(Python)

题目：[原题链接](https://leetcode-cn.com/problems/lru-cache-lcci/)（中等）

标签：设计、队列

| 解法           | 时间复杂度        | 空间复杂度 | 执行用时       |
| -------------- | ----------------- | ---------- | -------------- |
| Ans 1 (Python) | 所有操作 = $O(1)$ | $O(N)$     | 196ms (86.92%) |
| Ans 2 (Python) |                   |            |                |
| Ans 3 (Python) |                   |            |                |

解法一（双端队列）：

```python
class LRUCache:
    class Node:
        __slots__ = ("key", "value", "prev", "next")

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity

        # 定义当前缓存容量
        self.n = 0

        # 定义映射
        self.dict = {}

        # 定义双端队列
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.prev = self.tail
        self.tail.prev = self.head

    def _update(self, key):
        """将当前节点移动到队尾"""

        node = self.dict[key]

        # 从当前位置移除节点
        node.prev.next, node.next.prev = node.next, node.prev

        # 将节点添加到队尾
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.dict:
            self._update(key)
            return self.dict[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            if self.n >= self.capacity:
                # 移除双端链表中的第一个节点
                remove = self.head.next.key
                self.head.next.next.prev = self.head
                self.head.next = self.head.next.next

                # 删除映射
                del self.dict[remove]

                self.n -= 1

            # 添加新的节点
            node = self.Node(key, value)
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

            # 添加映射
            self.dict[key] = node

            self.n += 1

        else:
            self.dict[key].value = value
            self._update(key)
```