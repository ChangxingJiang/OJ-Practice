# LeetCode题解(0988)：寻找二叉树中从叶结点开始的最小字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/smallest-string-starting-from-leaf/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 56ms (90.91%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def smallestFromLeaf(self, root: TreeNode, now="") -> str:
        if not root:
            return ""
        ch = chr(97 + root.val)
        if root.left and root.right:
            left = self.smallestFromLeaf(root.left, ch + now)
            right = self.smallestFromLeaf(root.right, ch + now)
            return min(left, right)
        elif root.left:
            return self.smallestFromLeaf(root.left, ch + now)
        elif root.right:
            return self.smallestFromLeaf(root.right, ch + now)
        else:
            return ch + now
```

