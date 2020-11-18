# LeetCode题解(Offer55II)：判断二叉树是否为高度平衡的二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/)（简单）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 60ms (83.75%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = True

    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                self.ans = False
            return max(left, right) + 1

        dfs(root)

        return self.ans
```