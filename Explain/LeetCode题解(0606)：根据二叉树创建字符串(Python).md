# LeetCode题解(0606)：根据二叉树创建字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/construct-string-from-binary-tree/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

![LeetCode题解(0606)：截图1.png](LeetCode题解(0606)：截图1.png)

```python
def tree2str(self, t: TreeNode) -> str:
    def helper(node):
        if not node:
            return ""
        if node.left and node.right:
            return str(node.val) + "(" + helper(node.left) + ")(" + helper(node.right) + ")"
        elif node.left:
            return str(node.val) + "(" + helper(node.left) + ")"
        elif node.right:
            return str(node.val) + "()(" + helper(node.right) + ")"
        else:
            return str(node.val)

    return helper(t)
```