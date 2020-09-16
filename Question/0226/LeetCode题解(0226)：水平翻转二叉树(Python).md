# LeetCode题解(0226)：水平翻转二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/invert-binary-tree/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | O(n)       | O(n)       | 32ms (>96.33%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归翻转）：

```python
def invertTree(self, root: TreeNode) -> TreeNode:
    def helper(node):
        if not node:
            return None
        node.left, node.right = helper(node.right), helper(node.left)
        return node

    return helper(root)
```

