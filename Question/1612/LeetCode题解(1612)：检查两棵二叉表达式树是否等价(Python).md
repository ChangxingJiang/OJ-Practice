# LeetCode题解(1612)：检查两棵二叉表达式树是否等价(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-two-expression-trees-are-equivalent/)（中等）

标签：树、二叉树、深度优先搜索、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 536ms (79.31%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（哈希表）：

```python
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        count1, count2 = collections.Counter(), collections.Counter()
        self.dfs(root1, count1)
        self.dfs(root2, count2)
        return count1 == count2

    def dfs(self, node, count):
        if node:
            if not node.left and not node.right:
                count[node.val] += 1
            else:
                self.dfs(node.left, count)
                self.dfs(node.right, count)
```