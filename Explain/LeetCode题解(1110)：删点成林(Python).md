# LeetCode题解(1110)：删除二叉树中的指定点生成森林(Python)

题目：[原题链接](https://leetcode-cn.com/problems/delete-nodes-and-return-forest/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 100ms (30.00%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 72ms (98.33%)  |
| Ans 3 (Python) |            |            |                |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = []

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.ans.append(root)
        to_delete = set(to_delete)

        def dfs(node):
            if node:
                left = node.left
                right = node.right
                if node.val in to_delete:
                    if node in self.ans:
                        self.ans.remove(node)
                        to_delete.remove(node.val)
                    if node.left:
                        self.ans.append(node.left)
                    if node.right:
                        self.ans.append(node.right)
                else:
                    if node.left and node.left.val in to_delete:
                        node.left = None
                    if node.right and node.right.val in to_delete:
                        node.right = None
                if to_delete:
                    dfs(left)
                    dfs(right)

        dfs(root)
        return self.ans
```

解法二（优化解法一）；

```python
class Solution:
    def __init__(self):
        self.ans = []

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def dfs(node, delete):
            if node.left:
                if node.left.val in to_delete:
                    dfs(node.left, True)
                    node.left = None
                else:
                    if delete:
                        self.ans.append(node.left)
                    dfs(node.left, False)
            if node.right:
                if node.right.val in to_delete:
                    dfs(node.right, True)
                    node.right = None
                else:
                    if delete:
                        self.ans.append(node.right)
                    dfs(node.right, False)

        to_delete = set(to_delete)

        if not root:
            return []
        if not to_delete:
            return []

        if root.val in to_delete:
            self.ans = []
            dfs(root, True)
        else:
            self.ans = [root]
            dfs(root, False)

        return self.ans
```