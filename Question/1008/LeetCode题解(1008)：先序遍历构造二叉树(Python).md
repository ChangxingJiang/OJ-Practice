# LeetCode题解(1008)：先序遍历构造二叉搜索树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/)（中等）

标签：树、二叉树、二叉搜索树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (52.88%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder:
            root = TreeNode(preorder[0])
            i = 1
            while i < len(preorder) and preorder[i] < preorder[0]:
                i += 1
            root.left = self.bstFromPreorder(preorder[1:i])
            root.right = self.bstFromPreorder(preorder[i:])
            return root
```