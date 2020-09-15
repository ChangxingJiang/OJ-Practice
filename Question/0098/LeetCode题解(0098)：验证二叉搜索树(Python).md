# LeetCode题解(0098)：验证二叉搜索树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/validate-binary-search-tree/)（中等）

标签：数、二叉树、二叉搜索树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(logN)$  | 48ms (96.62%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isValidBST(self, root: TreeNode, left=float("-inf"), right=float("inf")) -> bool:
        if not root:
            return True
        if root.left:
            if not left < root.left.val < root.val:
                return False
            if not self.isValidBST(root.left, left=left, right=root.val):
                return False
        if root.right:
            if not root.val < root.right.val < right:
                return False
            if not self.isValidBST(root.right, left=root.val, right=right):
                return False
        return True
```

