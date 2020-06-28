# LeetCode题解(0404)：计算二叉树的左子叶之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-left-leaves/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(n)       | 44ms (65.99%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归）：

```python
def sumOfLeftLeaves(self, root: TreeNode) -> int:
    def helper(node, maybe=False):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            if maybe:
                return node.val
            else:
                return 0
        elif node.right is None:
            return helper(node.left, maybe=True)
        elif node.left is None:
            return helper(node.right)
        else:
            return helper(node.left, maybe=True) + helper(node.right)

    return helper(root)
```

