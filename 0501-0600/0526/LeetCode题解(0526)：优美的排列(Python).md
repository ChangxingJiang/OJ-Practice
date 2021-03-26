# LeetCode题解(0526)：优美的排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/beautiful-arrangement/)（中等）

标签：回溯算法、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N!)$    | $O(N)$     | 1804ms (20.71%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def __init__(self):
        self.N = 0
        self.ans = 0
        self.now = []

    def countArrangement(self, N: int) -> int:
        self.N = N
        self.now = [0] * (N + 1)
        self.dfs(1)
        return self.ans

    def dfs(self, i):
        if i == self.N + 1:
            self.ans += 1
        for j in range(1, self.N + 1):
            if self.now[j] == 0 and (i % j == 0 or j % i == 0):
                self.now[j] = i
                self.dfs(i + 1)
                self.now[j] = 0
```

