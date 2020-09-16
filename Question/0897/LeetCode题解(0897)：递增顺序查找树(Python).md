# LeetCode题解(0897)：递增顺序查找树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/increasing-order-search-tree/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (24.56%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 36ms (91.58%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（中序遍历）：

```python
def __init__(self):
    self.root = None
    self.last = None

def increasingBST(self, root: TreeNode) -> TreeNode:
    def helper(node):
        if node.left:
            helper(node.left)

        new_node = TreeNode(node.val)
        if self.root is None:
            self.root = self.last = new_node
        else:
            self.last.right = new_node
            self.last = self.last.right

        if node.right:
            helper(node.right)

    helper(root)

    return self.root
```

解法二（中序遍历）：

```python
def increasingBST(self, root: TreeNode) -> TreeNode:
    def helper(node):
        if node:
            yield from helper(node.left)
            yield node.val
            yield from helper(node.right)

    head = node = TreeNode(0)
    for val in helper(root):
        node.right = TreeNode(val)
        node = node.right

    return head.right
```