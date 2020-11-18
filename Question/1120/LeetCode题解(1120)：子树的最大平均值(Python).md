# LeetCode题解(1120)：子树的最大平均值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-average-subtree/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = 0

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if node:
            s1, n1 = self.dfs(node.left)
            s2, n2 = self.dfs(node.right)
            s, n = s1 + s2 + node.val, n1 + n2 + 1
            self.ans = max(self.ans, s / n)
            return s, n
        else:
            return 0, 0
```