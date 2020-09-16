# LeetCode题解(0700)：二叉搜索树中的搜索(Python)

题目：[原题链接](https://leetcode-cn.com/problems/search-in-a-binary-search-tree/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 84ms (96.08%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    def helper(node):
        if not node:
            return None
        if val == node.val:
            return node
        elif val < node.val:
            return helper(node.left)
        else:
            return helper(node.right)

    return helper(root)
```