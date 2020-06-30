# LeetCode题解(0687)：二叉树的最长同值路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-univalue-path/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 452ms (89.45%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def __init__(self):
    self.max = 0

def longestUnivaluePath(self, root: TreeNode) -> int:
    def helper(node):
        if not node:
            return 0

        left_length = 0
        right_length = 0
        if node.left:
            if node.val == node.left.val:
                left_length = helper(node.left) + 1
            else:
                helper(node.left)
        if node.right:
            if node.val == node.right.val:
                right_length = helper(node.right) + 1
            else:
                helper(node.right)
        if left_length > 0 and right_length > 0:
            self.max = max(self.max, left_length + right_length)

        else:
            self.max = max(self.max, left_length, right_length)
        return max(left_length, right_length)

    helper(root)

    return self.max
```