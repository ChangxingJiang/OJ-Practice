# LeetCode题解(0889)：从前序与后序遍历序列构造二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 64ms (84.29%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（递归）：

```python
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if pre:
            root = TreeNode(pre[0])

            if len(pre) == 1:
                return root

            idx = post.index(pre[1]) + 1  # 左子树节点数量

            root.left = self.constructFromPrePost(pre[1:idx + 1], post[:idx])
            root.right = self.constructFromPrePost(pre[idx + 1:], post[idx:-1])

            return root
```