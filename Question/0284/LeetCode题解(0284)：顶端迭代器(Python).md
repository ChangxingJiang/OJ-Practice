# LeetCode题解(0284)：顶端迭代器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/peeking-iterator/)（中等）

标签：设计

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(N)$     | 44ms (44.22%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.top = None

    def peek(self):
        if not self.top:
            self.top = self.iterator.next()
        return self.top

    def next(self):
        if not self.top:
            return self.iterator.next()
        else:
            ans, self.top = self.top, None
            return ans

    def hasNext(self):
        if self.top:
            return True
        else:
            return self.iterator.hasNext()
```

