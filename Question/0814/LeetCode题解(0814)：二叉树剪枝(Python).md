# LeetCode题解(0814)：依据指定规则对二叉树进行剪枝(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-pruning/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (56.95%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if root.val == 1 or root.left or root.right:
                return root
```