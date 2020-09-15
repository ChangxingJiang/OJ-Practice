# LeetCode题解(0951)：判断二叉树是否为翻转等价二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/flip-equivalent-binary-trees/)（中等）

标签：树、二叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(N1+N2)$ | 44ms (60.55%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # 处理两个节点均不存在的情况
        if not root1 and not root2:
            return True

        # 处理两个节点有一个存在的情况
        if not root1 or not root2:
            return False

        # 处理两个根节点不相等的情况
        if root1.val != root2.val:
            return False

        # 处理两个根节点相等的情况
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
```