# LeetCode题解(0617)：合并二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/merge-two-binary-trees/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 96ms (92.00%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    def helper(node1, node2):
        if node1 and node2:
            node = TreeNode(node1.val + node2.val)
            node.left = helper(node1.left, node2.left)
            node.right = helper(node1.right, node2.right)
            return node
        elif node1:
            return node1
        elif node2:
            return node2
        else:
            return None

    return helper(t1, t2)
```