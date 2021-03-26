# LeetCode题解(0285)：二叉搜索树中的顺序后继(Python)

题目：[原题链接](https://leetcode-cn.com/problems/inorder-successor-in-bst/)（中等）

标签：树、二叉树、二叉搜索树

| 解法           | 时间复杂度 | 空间复杂度  | 执行用时      |
| -------------- | ---------- | ----------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(log^2N)$ | 88ms (65.14%) |
| Ans 2 (Python) |            |             |               |
| Ans 3 (Python) |            |             |               |

解法一：

```python
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root or not p:
            return None

        return self.find([], root, p)

    def find(self, path, node, p):
        if node.val < p.val:
            return self.find(path + [node], node.right, p)
        elif node.val > p.val:
            return self.find(path + [node], node.left, p)
        else:
            # 目标节点有右子节点的情况
            if node.right:
                node = node.right
                while node.left:
                    node = node.left
                return node

            # 目标节点没有右子节点的情况
            else:
                while path and path[-1].val < node.val:
                    path.pop()
                if path:
                    return path.pop()
                else:
                    return None
```