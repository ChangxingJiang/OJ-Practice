# LeetCode题解(面试04.12)：求和路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/paths-with-sum-lcci/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 132ms (67.79%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = 0
        self.sum = 0
        self.total = 0
        self.lst = []

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        self.sum = sum

        self.dfs(root)

        return self.ans

    def dfs(self, node):
        self.total += node.val
        self.lst.append(node.val)

        last = 0
        for i in range(len(self.lst) - 1, -1, -1):
            last += self.lst[i]
            if last == self.sum:
                self.ans += 1

        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)

        # print(self.total, self.lst, self.ans)

        self.lst.pop()
        self.total -= node.val
```