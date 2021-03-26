# LeetCode题解(0538)：将二叉树转换为累加树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/convert-bst-to-greater-tree/)（简单）

与题目1038相同

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 76ms (87.34%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 68ms (98.52%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（反序中序遍历）：

```python
def __init__(self):
    self.total = 0

def convertBST(self, root: TreeNode) -> TreeNode:
    def helper(node):
        if not node:
            return 0
        helper(node.right)
        self.total += node.val
        node.val = self.total
        helper(node.left)

    helper(root)

    return root
```

解法二（解法一的优雅化）：

```python
def __init__(self):
    self.total = 0

def convertBST(self, root: TreeNode) -> TreeNode:
    if root:
        self.convertBST(root.right)
        self.total += root.val
        root.val = self.total
        self.convertBST(root.left)

    return root
```