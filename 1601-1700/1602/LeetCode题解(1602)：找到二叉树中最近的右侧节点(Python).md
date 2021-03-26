# LeetCode题解(1602)：找到二叉树中最近的右侧节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-nearest-right-node-in-binary-tree/)（中等）

标签：树、二叉树、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 392ms (13.79%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 336ms (51.72%) |
| Ans 3 (Python) |            |            |                |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = None

    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        self.dfs(root, u)
        return self.ans

    # 寻找目标节点
    def dfs(self, node, u):
        if not node:
            return -1
        if node == u:
            return 0
        else:
            left = self.dfs(node.left, u)
            if left != -1 and self.ans is None:
                self.dfs2(node.right, left + 1)
                return left + 1

            right = self.dfs(node.right, u)
            if right != -1:
                return right + 1

            return -1

    # 寻找目标节点的右侧节点（即寻找当前节点的等层最左侧节点）
    # O(logN)
    def dfs2(self, node, num):
        if node:
            if num == 1:
                self.ans = node
            else:
                if self.ans is None and node.left:
                    self.dfs2(node.left, num - 1)
                if self.ans is None and node.right:
                    self.dfs2(node.right, num - 1)
```

解法二（广度优先搜索）：

```python
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        now_level = collections.deque([root])
        while now_level:
            next_level = collections.deque()
            while now_level:
                node = now_level.popleft()
                if node == u:
                    if now_level:
                        return now_level.popleft()
                    else:
                        return None
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            now_level = next_level
        return None
```