# LeetCode题解(0669)：修剪二叉搜索树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/trim-a-binary-search-tree/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 56ms (93.19%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
    def helper(node):
        if not node:
            return None
        if L <= node.val <= R:
            node.left = helper(node.left)
            node.right = helper(node.right)
            return node
        elif node.val < L:
            return helper(node.right)
        elif node.val > R:
            return helper(node.left)

    return helper(root)
```