# LeetCode题解(Offer55I)：计算二叉树的最大深度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/)（简单）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (89.29%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
```