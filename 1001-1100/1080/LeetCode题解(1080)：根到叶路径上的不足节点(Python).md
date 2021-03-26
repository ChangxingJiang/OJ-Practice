# LeetCode题解(1080)：根到叶路径上的不足节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/insufficient-nodes-in-root-to-leaf-paths/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 116ms (32.88%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(now, node):
            if not node:
                return 0
            elif node.left and node.right:
                left = dfs(now + node.val, node.left)
                right = dfs(now + node.val, node.right)
                if now + node.val + left < limit:
                    node.left = None
                if now + node.val + right < limit:
                    node.right = None
                return node.val + max(left, right)
            elif node.left:
                left = dfs(now + node.val, node.left)
                return node.val + left
            elif node.right:
                right = dfs(now + node.val, node.right)
                return node.val + right
            else:
                return node.val

        val = dfs(0, root)
        return root if val >= limit else None
```

