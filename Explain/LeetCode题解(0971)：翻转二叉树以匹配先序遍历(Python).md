# LeetCode题解(0971)：翻转二叉树以匹配先序遍历(Python)

题目：[原题链接](https://leetcode-cn.com/problems/flip-binary-tree-to-match-preorder-traversal/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 68ms (5.80%)  |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 48ms (58.70%) |
| Ans 3 (Python) |            |            |               |

解法一（递归）：

```python
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        if not root:
            return []
        if root.val != voyage[0]:
            return [-1]

        if root.left and root.right:
            if root.left.val == voyage[1]:
                if root.right.val not in voyage[2:]:
                    return [-1]
                idx = voyage.index(root.right.val)
                left = self.flipMatchVoyage(root.left, voyage[1:idx])
                right = self.flipMatchVoyage(root.right, voyage[idx:])
                if left == [-1] or right == [-1]:
                    return [-1]
                else:
                    return left + right
            elif root.right.val == voyage[1]:
                if root.left.val not in voyage[2:]:
                    return [-1]
                idx = voyage.index(root.left.val)
                right = self.flipMatchVoyage(root.right, voyage[1:idx])
                left = self.flipMatchVoyage(root.left, voyage[idx:])
                if left == [-1] or right == [-1]:
                    return [-1]
                else:
                    return [root.val] + left + right

            else:
                return [-1]

        elif root.left:
            if root.left.val == voyage[1]:
                return self.flipMatchVoyage(root.left, voyage[1:])
            else:
                return [-1]

        elif root.right:
            if root.right.val == voyage[1]:
                return self.flipMatchVoyage(root.right, voyage[1:])
            else:
                return [-1]

        else:
            if len(voyage) == 1:
                return []
            else:
                return [-1]
```

解法二（优化解法一）：

```python
class Solution:
    def __init__(self):
        self.voyage = None
        self.ans = []
        self.i = 0

    def dfs(self, node):
        if node:
            # 处理根节点的值不相等的情况
            if node.val != self.voyage[self.i]:
                self.ans = [-1]
                return

            self.i += 1

            if node.left and self.i < len(self.voyage) and node.left.val != self.voyage[self.i]:
                self.ans.append(node.val)
                self.dfs(node.right)
                self.dfs(node.left)
            else:
                self.dfs(node.left)
                self.dfs(node.right)

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.voyage = voyage
        self.dfs(root)
        if self.ans and self.ans[0] == -1:
            return [-1]
        return self.ans
```