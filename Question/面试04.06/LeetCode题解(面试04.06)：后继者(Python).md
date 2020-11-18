# LeetCode题解(面试04.06)：二叉搜索树中指定节点的下一个节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/successor-lcci/)（中等）

标签：树、二叉树、二叉搜索树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 84ms (88.55%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（中序遍历）：

```python
class Solution:
    def __init__(self):
        self.aim = None
        self.ans = None
        self.this = False  # 上一个为目标节点

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        self.aim = p
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if node:
            self.dfs(node.left)

            if self.this:
                self.ans = node
                self.this = False
            else:
                if node == self.aim:
                    self.this = True

                if node.right:
                    self.dfs(node.right)
```