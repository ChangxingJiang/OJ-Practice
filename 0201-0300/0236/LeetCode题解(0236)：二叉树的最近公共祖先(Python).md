# LeetCode题解(0236)：寻找二叉树中两个节点的最近公共祖先(Python)

题目：[原题链接](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)（中等）

标签：树、二叉树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 100ms (33.46%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 88ms (74.28%)  |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursor(node):
            # 处理当前节点不存在的情况
            if not node:
                return False, False

            left = recursor(node.left)
            right = recursor(node.right)

            find_p = any([left[0], right[0], node.val == p.val])
            find_q = any([left[1], right[1], node.val == q.val])

            if find_p and find_q and not self.ans:
                self.ans = node

            return find_p, find_q

        recursor(root)

        return self.ans
```

解法二：

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 处理当前节点不存在的情况
        if not root:
            return root

        # 处理当前节点为p或q的情况
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 当左子树不包含目标节点时，返回右子树中找到的公共祖先
        if not left:
            return right

        # 当右子树不包含目标节点时，返回左子树中找到的公共祖先
        if not right:
            return left

        return root
```