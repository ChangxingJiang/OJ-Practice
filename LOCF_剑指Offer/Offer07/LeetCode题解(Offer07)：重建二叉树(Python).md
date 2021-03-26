# LeetCode题解(Offer07)：从前序与中序遍历序列构造二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 204ms (40.78%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 100ms (71.18%) |
| Ans 3 (Python) |            |            |                |

解法一（递归）：

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder and inorder:
            # 寻找当前二叉树的根节点
            val = preorder[0]
            root = TreeNode(val)

            # 寻找中序遍历中的根节点位置
            idx = inorder.index(val)

            # 处理左子树
            root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])

            # 处理右子树
            root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])

            # 返回当前树的结果
            return root
```

解法二（参数化递归）：

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recursor(p_left, p_right, i_left, i_right):
            if p_left < p_right and i_left < i_right:
                # 寻找当前二叉树的根节点
                val = preorder[p_left]
                root = TreeNode(val)

                # 寻找中序遍历中的根节点位置
                idx = inorder.index(val) - i_left

                # 处理左子树
                root.left = recursor(p_left + 1, p_left + idx + 1, i_left, i_left + idx)

                # 处理右子树
                root.right = recursor(p_left + idx + 1, p_right, i_left + idx + 1, i_right)

                # 返回当前树的结果
                return root

        return recursor(0, len(preorder), 0, len(inorder))
```