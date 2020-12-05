# LeetCode题解(LCP26)：导航装置(Python)

题目：[原题链接](https://leetcode-cn.com/problems/hSRGyL/)（困难）

标签：树、二叉树、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 896ms (94.74%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    # 对于每个三叉节点，至少有两边需要放导航

    def __init__(self):
        self.ans = 0

    def navigation(self, root: TreeNode) -> int:
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left == 0 and right == 0:
            return 1
        elif left == 2 or right == 2:
            return self.ans
        elif left == 1 and right == 1:
            return self.ans
        else:
            return self.ans + 1

    def dfs(self, node):
        """返回节点的上一个三叉路，有几个放置的导航"""
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if node.left and node.right:
            if left == 0 and right == 0:
                self.ans += 1
                return 1
            elif left == 0 or right == 0:
                return 1
            else:
                return 2
        elif node.left:
            return left
        elif node.right:
            return right
        else:
            return 0
```