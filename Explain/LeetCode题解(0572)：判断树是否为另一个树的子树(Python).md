# LeetCode题解(0572)：判断树是否为另一个树的子树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/subtree-of-another-tree/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 252ms (61.62%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法，两层递归）：

```python
def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    def inner_helper(node, aim):
        if node is None and aim is None:
            return True
        elif node is None or aim is None:
            return False
        return node.val == aim.val and inner_helper(node.left, aim.left) and inner_helper(node.right, aim.right)

    def helper(node):
        if node:
            if node.val == t.val:
                if inner_helper(node, t):
                    return True
            return helper(node.left) or helper(node.right)
        else:
            return False

    return helper(s)
```