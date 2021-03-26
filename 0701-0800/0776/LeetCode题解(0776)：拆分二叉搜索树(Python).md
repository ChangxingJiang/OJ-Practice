# LeetCode题解(0776)：拆分二叉搜索树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/split-bst/)（中等）

标签：树、二叉树、二叉搜索树、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 40ms (56.25%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（递归）：

```python
class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return [None, None]

        if V < root.val:
            left, right = self.splitBST(root.left, V)
            root.left = right
            return [left, root]
        elif root.val < V:
            left, right = self.splitBST(root.right, V)
            root.right = left
            return [root, right]
        else:
            right = root.right
            root.right = None
            return [root, right]
```