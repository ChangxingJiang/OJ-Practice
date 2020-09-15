# LeetCode题解(0979)：计算二叉树中依据指定规则分配硬币的最少移动次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/distribute-coins-in-binary-tree/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (88.55%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = 0

    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans += abs(left) + abs(right)
            return left + right + (node.val - 1)

        dfs(root)
        return self.ans
```