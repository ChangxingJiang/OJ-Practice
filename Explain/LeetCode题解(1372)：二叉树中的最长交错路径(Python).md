# LeetCode题解(1372)：计算二叉树中的最长交错路径的长度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-zigzag-path-in-a-binary-tree/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 492ms (74.21%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 532ms (55.66%) |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def __init__(self):
        self.max = 0

    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            if node.left and node.right:
                left = dfs(node.left)[1]
                right = dfs(node.right)[0]
                self.max = max(self.max, left, right)
                return left + 1, right + 1
            elif node.left:
                left = dfs(node.left)[1]
                right = 0
                self.max = max(self.max, left)
                return left + 1, right + 1
            elif node.right:
                left = 0
                right = dfs(node.right)[0]
                self.max = max(self.max, right)
                return left + 1, right + 1
            else:
                return 1, 1

        dfs(root)

        return self.max
```

解法二（调整解法一逻辑）：

```python
class Solution:
    def __init__(self):
        self.max = 0

    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0

            if node.left:
                left = dfs(node.left)[1]
            else:
                left = 0

            if node.right:
                right = dfs(node.right)[0]
            else:
                right = 0

            self.max = max(self.max, left, right)

            return left + 1, right + 1

        dfs(root)

        return self.max
```



