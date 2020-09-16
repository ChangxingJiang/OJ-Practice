# LeetCode题解(0701)：二叉搜索树中的插入操作(Python)

题目：[原题链接](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/)（中等）

| 解法           | 时间复杂度           | 空间复杂度          | 执行用时       |
| -------------- | -------------------- | ------------------- | -------------- |
| Ans 1 (Python) | $O(H)$ : H为树的高度 | $O(H)$: H为树的高度 | 156ms (89.91%) |
| Ans 2 (Python) | $O(H)$ : H为树的高度 | $O(H)$: H为树的高度 | 160ms (83.03%) |
| Ans 3 (Python) |                      |                     |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    def helper(node):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                helper(node.left)
        if val > node.val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                helper(node.right)

    if root is None:
        return TreeNode(val)
    else:
        helper(root)
        return root
```

解法二（优雅版解法一）：

```python
def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = self.insertIntoBST(root.left, val)
    else:
        root.right = self.insertIntoBST(root.right, val)
    return root
```