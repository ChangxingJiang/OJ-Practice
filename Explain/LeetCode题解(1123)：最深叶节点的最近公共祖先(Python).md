# LeetCode题解(1123)：计算二叉树中最深叶节点的最近公共祖先(Python)

题目：[原题链接](https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×H)$   | $O(N)$     | 76ms (32.12%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 72ms (33.32%) |
| Ans 3 (Python) | $O(N)$     | $O(N)$     | 56ms (92.23%) |

解法一：

```python
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        # 计算二叉树的最大深度
        def max_depth(node):
            if not node:
                return 0
            return max(max_depth(node.left), max_depth(node.right)) + 1

        def recursor(node):
            depth_left = max_depth(node.left)
            depth_right = max_depth(node.right)
            if depth_left == depth_right:
                return node
            else:
                return recursor(node.left) if depth_left > depth_right else recursor(node.right)

        return recursor(root)
```

解法二（哈希表记录最大深度）：

```python
class Solution:
    def __init__(self):
        self.hashmap = {}

    def max_depth(self, node):
        if not node:
            return 0
        if node in self.hashmap:
            return self.hashmap[node]
        else:
            depth = max(self.max_depth(node.left), self.max_depth(node.right)) + 1
            self.hashmap[node] = depth
            return depth

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        depth_left = self.max_depth(root.left)
        depth_right = self.max_depth(root.right)
        if depth_left == depth_right:
            return root
        elif depth_left > depth_right:
            return self.lcaDeepestLeaves(root.left)
        else:
            return self.lcaDeepestLeaves(root.right)
```

解法三：

```python
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node, depth):
            if not node:
                return None, 0
            if not node.left and not node.right:
                return node, depth
            left, depth_left = dfs(node.left, depth + 1)
            right, depth_right = dfs(node.right, depth + 1)
            if depth_left == depth_right:
                return node, depth_left
            elif depth_left > depth_right:
                return left, depth_left
            else:
                return right, depth_right

        return dfs(root, 1)[0]
```