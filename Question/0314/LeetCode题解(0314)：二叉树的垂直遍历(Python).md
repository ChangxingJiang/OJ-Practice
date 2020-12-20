# LeetCode题解(0314)：二叉树的垂直遍历(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-vertical-order-traversal/)（中等）

标签：树、二叉树、深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 48ms (28.81%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.min_idx = 0
        self.max_idx = 0
        self.ans = collections.deque([[]])

    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        self.dfs(root, 0, 0)

        ans = []
        for level in self.ans:
            level.sort(key=lambda x: x[0])
            ans.append([elem[1] for elem in level])

        return ans

    def dfs(self, node, idx, h):
        if node:
            if idx < self.min_idx:
                self.min_idx -= 1
                self.ans.appendleft([])
            elif idx > self.max_idx:
                self.max_idx += 1
                self.ans.append([])
            actual_idx = idx - self.min_idx
            self.ans[actual_idx].append((h, node.val))

            self.dfs(node.left, idx - 1, h + 1)
            self.dfs(node.right, idx + 1, h + 1)
```