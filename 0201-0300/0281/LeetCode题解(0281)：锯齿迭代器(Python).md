# LeetCode题解(0281)：锯齿迭代器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/zigzag-iterator/)（中等）

标签：设计、数组

| 解法           | 时间复杂度                    | 空间复杂度 | 执行用时      |
| -------------- | ----------------------------- | ---------- | ------------- |
| Ans 1 (Python) | 构造 = $O(1)$ ; 迭代 = $O(1)$ | $O(1)$     | 56ms (90.24%) |
| Ans 2 (Python) |                               |            |               |
| Ans 3 (Python) |                               |            |               |

解法一：

```python
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v = [v1, v2]
        self.size = max(len(v1), len(v2))
        self.i = 0
        self.j = 0
        self._find_next()

    def _find_next(self):
        if self.i == 2:
            self.i = 0
            self.j += 1
        while self.size > self.j >= len(self.v[self.i]):
            self.i += 1
            if self.i == 2:
                self.i = 0
                self.j += 1

    def next(self) -> int:
        if self.j < self.size:
            val = self.v[self.i][self.j]
            self.i += 1
            self._find_next()
            return val
        else:
            return -1

    def hasNext(self) -> bool:
        return self.j < self.size
```