# LeetCode题解(0250)：统计同值子树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-univalue-subtrees/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(logN)$  | 48ms (44.68%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = 0

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.dfs(root)

        return self.ans

    def dfs(self, node):
        if node.left and node.right:
            v1 = self.dfs(node.left)
            v2 = self.dfs(node.right)
            if v1 is not None and v2 is not None and node.val == v1 == v2:
                self.ans += 1
                return node.val
            else:
                return None
        elif node.left:
            v = self.dfs(node.left)
            if v is not None and node.val == v:
                self.ans += 1
                return node.val
            else:
                return None
        elif node.right:
            v = self.dfs(node.right)
            if v is not None and node.val == v:
                self.ans += 1
                return node.val
            else:
                return None
        else:
            self.ans += 1
            return node.val
```