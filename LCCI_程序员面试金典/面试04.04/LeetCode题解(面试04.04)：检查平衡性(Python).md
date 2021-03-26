# LeetCode题解(面试04.04)：检查二叉树的平衡性(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-balance-lcci/)（简单）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (99.41%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = True

    def isBalanced(self, root: TreeNode) -> bool:
        self.dfs(root)
        return self.ans

    def dfs(self, root: TreeNode):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if abs(right - left) > 1:
            self.ans = False
        return max(left,right) + 1
```