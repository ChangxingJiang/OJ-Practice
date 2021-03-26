# LeetCode题解(0366)：寻找二叉树的叶子节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-leaves-of-binary-tree/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 36ms (88.24%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = []

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if node:
            height = 1 + max(self.dfs(node.left), self.dfs(node.right))
            if len(self.ans) < height:
                self.ans.append([])
            self.ans[height - 1].append(node.val)
            return height
        else:
            return 0
```