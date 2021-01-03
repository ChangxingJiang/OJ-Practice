# LeetCode题解(1656)：设计有序流(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-an-ordered-stream/)（简单）

标签：设计、数组

| 解法           | 时间复杂度                        | 空间复杂度 | 执行用时       |
| -------------- | --------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | 初始化 = $O(N)$ ; insert = $O(L)$ | $O(N)$     | 184ms (45.19%) |
| Ans 2 (Python) |                                   |            |                |
| Ans 3 (Python) |                                   |            |                |

解法一：

```python
class OrderedStream:

    def __init__(self, n: int):
        self.array = [""] * n
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.array[id - 1] = value
        res = []
        while self.ptr < len(self.array) and self.array[self.ptr] != "":
            res.append(self.array[self.ptr])
            self.ptr += 1
        return res
```

