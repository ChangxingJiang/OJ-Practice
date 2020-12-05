# LeetCode题解(1382)：将二叉搜索树变平衡(Python)

题目：[原题链接](https://leetcode-cn.com/problems/balance-a-binary-search-tree/)（中等）

标签：树、二叉树、二叉搜索树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 240ms (79.27%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def inorder(self, node, lst):
        if node:
            self.inorder(node.left, lst)
            lst.append(node.val)
            self.inorder(node.right, lst)

    def balanceBST(self, root: TreeNode) -> TreeNode:
        lst = []
        self.inorder(root, lst)
        size = len(lst)
        return self.dfs(lst, 0, size - 1)

    def dfs(self, lst, l, r):
        if l > r:
            return None
        if l == r:
            return TreeNode(lst[l])
        else:
            m = (l + r) // 2
            root = TreeNode(lst[m])
            root.left = self.dfs(lst, l, m - 1)
            root.right = self.dfs(lst, m + 1, r)
            return root
```