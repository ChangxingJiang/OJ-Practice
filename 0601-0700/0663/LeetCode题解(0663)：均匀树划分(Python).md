# LeetCode题解(0663)：均匀树划分(Python)

题目：[原题链接](https://leetcode-cn.com/problems/equal-tree-partition/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 80ms (90.91%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.vals = set()

    def checkEqualTree(self, root: TreeNode) -> bool:
        total = root.val + self.dfs(root.left) + self.dfs(root.right)  # 根节点不能是答案
        return total / 2 in self.vals

    def dfs(self, node):
        if node:
            v = node.val + self.dfs(node.left) + self.dfs(node.right)
            self.vals.add(v)
            return v
        else:
            return 0
```