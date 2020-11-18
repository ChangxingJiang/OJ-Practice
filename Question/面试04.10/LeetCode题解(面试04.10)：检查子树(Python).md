# LeetCode题解(面试04.10)：检查二叉树是否为另一个二叉树的子树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-subtree-lcci/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^N)$   | $O(N)$     | 116ms (80.85%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（深度优先搜索）：

```python
class Solution:
    def maybe_find(self, n1, n2):
        if not n1 and not n2:
            return True
        elif not n1 or not n2:
            return False
        elif n1.val != n2.val:
            return False
        else:
            return self.maybe_find(n1.left, n2.left) and self.maybe_find(n1.right, n2.right)

    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t2:
            return True
        elif not t1:
            return False
        elif t1.val == t2.val and self.maybe_find(t1, t2):
            return True
        else:
            return self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)
```