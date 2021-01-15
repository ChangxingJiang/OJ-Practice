# LeetCode题解(0386)：字典序排数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/lexicographical-numbers/)（中等）

标签：深度优先搜索、递归、回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 144ms (46.12%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 272ms (12.00%) |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return [int(i) for i in sorted(str(i) for i in range(1,n+1))]
```

解法二：

```python
class Solution:
    def __init__(self):
        self.ans = []
        self.n = 0

    def lexicalOrder(self, n: int) -> List[int]:
        self.n = n

        for i in range(1, 10):
            self.dfs(i)

        return self.ans

    def dfs(self, i):
        if i <= self.n:
            self.ans.append(i)
            for j in range(0, 10):
                self.dfs(i * 10 + j)
```

