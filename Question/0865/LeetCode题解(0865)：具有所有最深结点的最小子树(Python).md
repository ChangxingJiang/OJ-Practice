# LeetCode题解(0865)：寻找二叉树中具有所有最深结点的最小子树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/smallest-subtree-with-all-the-deepest-nodes/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度                         | 空间复杂度 | 执行用时      |
| -------------- | ---------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×H)$ : 其中H为二叉树的最大深度 | $O(N)$     | 48ms (62.87%) |
| Ans 2 (Python) | $O(N)$                             | $O(N)$     | 56ms (21.56%) |
| Ans 3 (Python) |                                    |            |               |

解法一：

```python
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
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

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth_left = self.max_depth(root.left)
        depth_right = self.max_depth(root.right)
        if depth_left == depth_right:
            return root
        elif depth_left > depth_right:
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)
```