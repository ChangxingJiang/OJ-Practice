# LeetCode题解(0510)：二叉搜索树中的中序后继(Python)

题目：[原题链接](https://leetcode-cn.com/problems/inorder-successor-in-bst-ii/)（中等）

标签：树、二叉树、二叉搜索树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 92ms (82.20%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        else:
            now = node.val
            while node.parent:
                node = node.parent
                if node.val > now:
                    return node
                elif node.right and node.right.val > now:
                    node = node.right
                    while node.left:
                        node = node.left
                    return node
        return None
```

