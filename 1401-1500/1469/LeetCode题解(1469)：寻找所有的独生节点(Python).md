# LeetCode题解(1469)：寻找所有的独生节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-all-the-lonely-nodes/)（简单）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (98.00%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = []

    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if node.left and node.right:
            self.dfs(node.left)
            self.dfs(node.right)
        elif node.left:
            self.ans.append(node.left.val)
            self.dfs(node.left)
        elif node.right:
            self.ans.append(node.right.val)
            self.dfs(node.right)
```