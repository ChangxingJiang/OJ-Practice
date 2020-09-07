# LeetCode题解(0106)：从中序与后序遍历序列构造二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 220ms (22.59%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 112ms (74.77%) |
| Ans 3 (Python) |            |            |                |

解法一（递归）：

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if postorder and inorder:
            # 寻找当前二叉树的根节点
            val = postorder[-1]
            root = TreeNode(val)

            # 寻找中序遍历中的根节点位置
            idx = inorder.index(val)

            # 处理左子树
            root.left = self.buildTree(inorder[:idx], postorder[:idx])

            # 处理右子树
            root.right = self.buildTree(inorder[idx + 1:], postorder[idx:-1])

            # 返回当前树的结果
            return root
```

解法二（参数化递归）：

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def recursor(i_left, i_right, p_left, p_right):
            if i_left < i_right and p_left < p_right:
                # 寻找当前二叉树的根节点
                val = postorder[p_right - 1]
                root = TreeNode(val)

                # 寻找中序遍历中的根节点位置
                idx = inorder.index(val) - i_left

                # 处理左子树
                root.left = recursor(i_left, i_left + idx, p_left, p_left + idx)

                # 处理右子树
                root.right = recursor(i_left + idx + 1, i_right, p_left + idx, p_right - 1)

                # 返回当前树的结果
                return root

        return recursor(0, len(inorder), 0, len(postorder))
```