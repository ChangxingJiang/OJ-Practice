# LeetCode题解(0543)：计算二叉树的直径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/diameter-of-binary-tree/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(N)       | O(N)       | 52ms (88.88%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def __init__(self):
    self.maximum = 0

def diameterOfBinaryTree(self, root: TreeNode) -> int:
    def depth(node):
        if node is None:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        maximum = left + right
        if maximum > self.maximum:
            self.maximum = maximum
        return max(left, right) + 1

    depth(root)
    return self.maximum
```

