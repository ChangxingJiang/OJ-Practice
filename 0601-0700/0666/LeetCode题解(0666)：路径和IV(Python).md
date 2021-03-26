# LeetCode题解(0666)：路径和IV(Python)

题目：[原题链接](https://leetcode-cn.com/problems/path-sum-iv/)（中等）

标签：树、二叉树、深度优先搜素

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(15)$    | 28ms (25.27%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.lst = [[-1] * (2 ** i) for i in range(4)]

    def pathSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        for num in nums:
            a, b, c = num // 100 - 1, num % 100 // 10 - 1, num % 10
            self.lst[a][b] = c

        return self.dfs(0, 0, 0)

    def dfs(self, now, a, b):
        v = self.lst[a][b]
        if a == 3:
            return now + v
        elif self.lst[a + 1][b * 2] != -1 and self.lst[a + 1][b * 2 + 1] != -1:
            return self.dfs(now + v, a + 1, b * 2) + self.dfs(now + v, a + 1, b * 2 + 1)
        elif self.lst[a + 1][b * 2] != -1:
            return self.dfs(now + v, a + 1, b * 2)
        elif self.lst[a + 1][b * 2 + 1] != -1:
            return self.dfs(now + v, a + 1, b * 2 + 1)
        else:
            return now + v
```