# LeetCode题解(0257)：计算二叉树的所有路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-paths/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(n)       | 36ms (92.22%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归遍历树实现）：

```python
def binaryTreePaths(self, root: TreeNode) -> List[str]:

    def helper(node, path=None):
        if path:
            path += "->" + str(node.val)
        else:
            path = str(node.val)
        if node.left and node.right:
            return helper(node.left, path) + helper(node.right, path)
        elif node.left:
            return helper(node.left, path)
        elif node.right:
            return helper(node.right, path)
        else:
            return [path]

    if root:
        return helper(root)
    else:
        return []
```