# LeetCode题解(0938)：二叉搜索树的范围和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/range-sum-of-bst/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(H)$     | 248ms (83.98%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```
def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    def helper(node):
        if not node:
            return 0
        ans = 0
        if L <= node.val <= R:
            ans += node.val
        if L < node.val:
            ans += helper(node.left)
        if R > node.val:
            ans += helper(node.right)
        return ans

    return helper(root)
```