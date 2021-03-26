# LeetCode题解(0530)：二叉搜索树的最小绝对差(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/)（简单）

与题目783相同

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(1)       | 76ms (38.05%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（中序遍历）：

```python
def __init__(self):
    self.minimum = float("inf")
    self.last = float("-inf")

def getMinimumDifference(self, root: TreeNode) -> int:
    def helper(node):
        if node:
            helper(node.left)

            self.minimum = min(self.minimum, node.val - self.last)
            self.last = node.val

            helper(node.right)

    helper(root)

    return int(self.minimum)
```

