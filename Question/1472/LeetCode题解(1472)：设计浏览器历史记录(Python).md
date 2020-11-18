# LeetCode题解(1472)：设计浏览器历史记录(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-browser-history/)（中等）

标签：设计、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(1)$     | $O(N)$     | 200ms (96%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0
        self.size = 1
        self.array = collections.deque([homepage])

    def visit(self, url: str) -> None:
        self.i += 1
        if self.i == len(self.array):
            self.array.append(url)
        else:
            self.array[self.i] = url
        self.size = self.i + 1

    def back(self, steps: int) -> str:
        self.i -= steps
        if self.i < 0:
            self.i = 0
        return self.array[self.i]

    def forward(self, steps: int) -> str:
        self.i += steps
        if self.i >= self.size:
            self.i = self.size - 1
        return self.array[self.i]
```