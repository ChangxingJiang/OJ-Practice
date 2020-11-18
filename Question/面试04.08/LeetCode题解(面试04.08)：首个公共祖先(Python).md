# LeetCode题解(面试04.08)：首个公共祖先(Python)

题目：[原题链接](https://leetcode-cn.com/problems/first-common-ancestor-lcci/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 76ms (93.28%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.dfs(root, p, q)
        return self.ans

    def dfs(self, root: TreeNode, p: TreeNode, q: TreeNode):
        if not root:
            return 0
        else:
            left = self.dfs(root.left, p, q)
            right = self.dfs(root.right, p, q)
            this = 1 if root == p or root == q else 0
            if left == 2 or right == 2:
                return 2
            elif (left + right + this) == 2:
                self.ans = root
                return 2
            else:
                return left + right + this
```