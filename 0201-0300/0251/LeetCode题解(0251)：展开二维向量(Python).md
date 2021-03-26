# LeetCode题解(0251)：展开二维向量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/flatten-2d-vector/)（中等）

标签：设计、数组

| 解法           | 时间复杂度        | 空间复杂度 | 执行用时      |
| -------------- | ----------------- | ---------- | ------------- |
| Ans 1 (Python) | 每次操作 = $O(1)$ | $O(1)$     | 96ms (64.00%) |
| Ans 2 (Python) |                   |            |               |
| Ans 3 (Python) |                   |            |               |

解法一：

```python
class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = v
        self.i = 0
        self.j = 0
        self._find_next()

    def next(self) -> int:
        res = self.v[self.i][self.j]
        self.j += 1
        self._find_next()
        return res

    def hasNext(self) -> bool:
        return self._find_next()

    def _find_next(self):
        while self.i < len(self.v) and self.j >= len(self.v[self.i]):
            self.i += 1
            self.j = 0
        return self.i < len(self.v)
```