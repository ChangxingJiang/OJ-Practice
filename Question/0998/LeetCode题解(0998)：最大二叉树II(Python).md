# LeetCode题解(0998)：构造最大二叉树(每个节点的值都大于其子树中的任何其他值)(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-binary-tree-ii/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (79.59%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        # 处理目标值大于根节点的情况
        if val > root.val:
            new = TreeNode(val)
            new.left = root
            return new

        # 处理目标值小于根节点的情况
        last = root
        node = root.right
        while node and val < node.val:
            last = node
            node = node.right
        new = TreeNode(val)
        new.left = node
        last.right = new
        return root
```