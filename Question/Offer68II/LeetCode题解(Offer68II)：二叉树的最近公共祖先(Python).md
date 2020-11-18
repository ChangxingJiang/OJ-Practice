# LeetCode题解(Offer68II)：寻找二叉树中两个节点的最近公共祖先(Python)

题目：[原题链接](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/)（简单）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 96ms (40.89%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 76ms (97.61%) |
| Ans 3 (Python) |            |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node, pp, qq):
            if node:
                now = dfs(node.left, pp, qq) + dfs(node.right, pp, qq) + (node.val == pp.val) + (node.val == qq.val)
                if now == 2:
                    if not self.ans:
                        self.ans = node
                return now
            else:
                return False

        dfs(root, p, q)

        return self.ans
```

解法二：

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root:
            if root == p or root == q:
                return root
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if not left:
                return right
            if not right:
                return left
            return root
```