# LeetCode题解(1188)：设计有限阻塞队列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-bounded-blocking-queue/)（中等）

标签：多线程、设计、队列

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(N)$     | 52ms (68.63%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
import threading


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.en = threading.Semaphore(capacity)
        self.de = threading.Semaphore(0)
        self.queue = collections.deque()
        self.n = 0

    def enqueue(self, element: int) -> None:
        self.n += 1
        self.en.acquire()
        self.queue.appendleft(element)
        self.de.release()

    def dequeue(self) -> int:
        self.n -= 1
        self.de.acquire()
        val = self.queue.pop()
        self.en.release()
        return val

    def size(self) -> int:
        return self.n
```