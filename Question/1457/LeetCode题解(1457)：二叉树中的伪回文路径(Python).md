# LeetCode题解(1457)：计算二叉树中的伪回文路径数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree/)（中等）

标签：树、二叉树、深度优先搜索、位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 492ms (70.81%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = 0

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def dfs(node, last=0):
            if node:
                last ^= 1 << (node.val - 1)
                if node.left or node.right:
                    dfs(node.left, last)
                    dfs(node.right, last)
                else:
                    num = 0
                    while last:
                        num += last & 1
                        last >>= 1
                    if num <= 1:
                        self.ans += 1

        dfs(root)

        return self.ans
```