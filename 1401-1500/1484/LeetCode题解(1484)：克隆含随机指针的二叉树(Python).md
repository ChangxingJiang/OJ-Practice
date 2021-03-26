# LeetCode题解(1484)：克隆含随机指针的二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/clone-binary-tree-with-random-pointer/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 240ms (96.67%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（两次深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.hashmap = {}

    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return None

        # 深度优先搜索构造忽略随机指针的二叉树和哈希字典
        # O(N)
        ans = NodeCopy(root.val)
        self.dfs1(root, ans)

        # 深度优先搜索构造随机指针
        # O(N)
        self.dfs2(root, ans)

        return ans

    def dfs1(self, node, copy):
        self.hashmap[node] = copy
        if node.left:
            copy.left = NodeCopy(node.left.val)
            self.dfs1(node.left, copy.left)
        if node.right:
            copy.right = NodeCopy(node.right.val)
            self.dfs1(node.right, copy.right)

    def dfs2(self, node, copy):
        if node.random:
            copy.random = self.hashmap[node.random]
        if node.left:
            self.dfs2(node.left, copy.left)
        if node.right:
            self.dfs2(node.right, copy.right)
```