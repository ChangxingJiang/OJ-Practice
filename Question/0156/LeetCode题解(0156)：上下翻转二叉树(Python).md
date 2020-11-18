# LeetCode题解(0156)：上下翻转二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-upside-down/)（中等）

标签：树、二叉树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (82.61%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        ans = TreeNode(root.val)
        while root.left:
            node = TreeNode(root.left.val)
            node.right = ans
            node.left = root.right
            ans = node
            root = root.left
        return ans
```