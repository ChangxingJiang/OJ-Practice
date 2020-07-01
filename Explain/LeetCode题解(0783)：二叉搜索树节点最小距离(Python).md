# LeetCode题解(0783)：二叉搜索树节点最小距离(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/)（简单）

本题与题目530重复

| 解法           | 时间复杂度 | 空间复杂度           | 执行用时      |
| -------------- | ---------- | -------------------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(H)$ : H为树的高度 | 36ms (92.46%) |
| Ans 2 (Python) |            |                      |               |
| Ans 3 (Python) |            |                      |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def __init__(self):
    self.min = float("inf")
    self.last = float("-inf")

def minDiffInBST(self, root: TreeNode) -> int:
    def helper(node):
        if not node:
            return []

        left = helper(node.left)

        self.min = min(self.min, node.val - self.last)
        self.last = node.val

        right = helper(node.right)

        return left + [node.val] + right

    helper(root)

    return int(self.min)
```