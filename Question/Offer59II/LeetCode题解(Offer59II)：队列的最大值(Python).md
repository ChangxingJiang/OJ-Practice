# LeetCode题解(Offer59II)：设计可以在常数时间内返回最大值的队列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/)（中等）

标签：队列、设计、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(1)$     | $O(N)$     | 328ms (38.65%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（双队列实现）：

```python
class MaxQueue:

    def __init__(self):
        self.queue = collections.deque()  # 数据存储队列
        self.most_queue = collections.deque()  # 最大值队列

    def max_value(self) -> int:
        return self.most_queue[0] if self.most_queue else -1

    def push_back(self, value: int) -> None:
        while self.most_queue and self.most_queue[-1] < value:
            self.most_queue.pop()
        self.most_queue.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        value = self.queue.popleft()
        if value == self.most_queue[0]:
            self.most_queue.popleft()
        return value
```