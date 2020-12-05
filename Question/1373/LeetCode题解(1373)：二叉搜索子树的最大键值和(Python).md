# LeetCode题解(1373)：二叉搜索子树的最大键值和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree/)（困难）

标签：树、二叉树、二叉搜索树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 476ms (42.39%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = 0

    def maxSumBST(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return True, 0, float("inf"), float("-inf")
        else:
            # 遍历两棵子树
            bool1, val1, l1, l2 = self.dfs(node.left)
            bool2, val2, r1, r2 = self.dfs(node.right)

            # 判断两棵子树是否符合二叉搜索树性质
            if not bool1 or not bool2:
                return False, -1, 0, 0

            # 判断当前节点是否符合二叉搜索树性质
            if node.val <= l2 or node.val >= r1:
                return False, -1, 0, 0

            l = l1 if node.left else node.val
            r = r2 if node.right else node.val

            val = val1 + node.val + val2
            self.ans = max(self.ans, val)
            return True, val, l, r
```