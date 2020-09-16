# LeetCode题解(1325)：删除二叉树中指定值的叶子节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/delete-leaves-with-a-given-value/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 68ms (58.44%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(node):
            if node.left and dfs(node.left):
                node.left = None
            if node.right and dfs(node.right):
                node.right = None
            return not node.left and not node.right and node.val == target

        dfs(root)

        if not root.left and not root.right and root.val == target:
            return None

        return root

```