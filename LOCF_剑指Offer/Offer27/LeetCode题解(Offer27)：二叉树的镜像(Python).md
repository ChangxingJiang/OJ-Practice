# LeetCode题解(Offer27)：左右翻转一颗二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/)（简单）

标签：树、二叉树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (73.73%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
            return root
```