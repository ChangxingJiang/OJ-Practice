# LeetCode题解(0298)：二叉树最长连续序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 100ms (99.39%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = 0

    def longestConsecutive(self, root: TreeNode) -> int:
        self.dfs(root, 0, float("NAN"))
        return self.ans

    def dfs(self, node, now_length, now_val):
        if node:
            if node.val == now_val + 1:
                self.ans = max(self.ans, now_length + 1)
                self.dfs(node.left, now_length + 1, node.val)
                self.dfs(node.right, now_length + 1, node.val)
            else:
                self.ans = max(self.ans, 1)
                self.dfs(node.left, 1, node.val)
                self.dfs(node.right, 1, node.val)
```