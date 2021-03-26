# LeetCode题解(面试04.05)：检查二叉搜索树是否合法(Python)

题目：[原题链接](https://leetcode-cn.com/problems/legal-binary-search-tree-lcci/)（中等）

标签：树、二叉树、二叉搜索树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (88.10%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = True

    def isValidBST(self, root: TreeNode) -> bool:
        self.dfs(root)
        return self.ans

    def dfs(self, root: TreeNode, min_val=float("-inf"), max_val=float("inf")):
        if root:
            if root.left and root.right:
                if not min_val < root.left.val < root.val < root.right.val < max_val:
                    self.ans = False
                else:
                    self.dfs(root.left, min_val=min_val, max_val=root.val)
                    self.dfs(root.right, min_val=root.val, max_val=max_val)
            elif root.left:
                if not min_val < root.left.val < root.val < max_val:
                    self.ans = False
                else:
                    self.dfs(root.left, min_val=min_val, max_val=root.val)
            elif root.right:
                if not min_val < root.val < root.right.val < max_val:
                    self.ans = False
                else:
                    self.dfs(root.right, min_val=root.val, max_val=max_val)
```