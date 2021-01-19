# LeetCode题解(0900)：RLE迭代器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rle-iterator/)（中等）

标签：数组、设计

| 解法           | 时间复杂度                           | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | RLEIterator = $O(A)$ ; next = $O(N)$ | $O(A)$     | 48ms (55.38%) |
| Ans 2 (Python) |                                      |            |               |
| Ans 3 (Python) |                                      |            |               |

解法一：

```python
class RLEIterator:

    def __init__(self, A: List[int]):
        self.lst = []
        for i in range(0, len(A), 2):
            if A[i] > 0:
                self.lst.append([A[i + 1], A[i]])
        self.lst.reverse()
        print(self.lst)

    def next(self, n: int) -> int:
        while self.lst:
            val, num = self.lst.pop()
            if num < n:
                n -= num
            elif num == n:
                return val
            else:
                num -= n
                self.lst.append([val, num])
                return val
        return -1
```

