# LeetCode题解(0965)：判断是否为单值二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/univalued-binary-tree/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 36ms (90.72%) |
| Ans 2 (Python) | $O(n)$     | $O(H)$     | 40ms (77.25%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（迭代）：

```python
def isUnivalTree(self, root: TreeNode) -> bool:
    val = root.val
    now_node = [root]
    while now_node:
        next_node = []
        for node in now_node:
            if node.val != val:
                return False
            if node.left:
                next_node.append(node.left)
            if node.right:
                next_node.append(node.right)
        now_node = next_node
    return True
```

解法二（递归）：

```python
def __init__(self):
    self.val = None

def isUnivalTree(self, root: TreeNode) -> bool:
    self.val = root.val

    def helper(node):
        if not node:
            return True
        elif node.val != self.val:
            return False
        else:
            return helper(node.left) and helper(node.right)

    return helper(root)
```