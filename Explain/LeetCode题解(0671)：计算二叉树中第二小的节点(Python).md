# LeetCode题解(0671)：计算二叉树中第二小的节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 20ms (99.85%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

![LeetCode题解(0671)：截图1.png](LeetCode题解(0671)：截图1.png)

```python
def __init__(self):
    self.min1 = float("inf")
    self.min2 = float("inf")

def findSecondMinimumValue(self, root: TreeNode) -> int:
    def helper(node):
        if node.val < self.min1:
            self.min2 = self.min1
            self.min1 = node.val
        elif self.min1 < node.val < self.min2:
            self.min2 = node.val
        if node.left and node.right:
            if node.left.val < self.min2:
                helper(node.left)
            if node.right.val < self.min2:
                helper(node.right)

    helper(root)

    if self.min2 == float("inf"):
        return -1
    else:
        return int(self.min2)
```