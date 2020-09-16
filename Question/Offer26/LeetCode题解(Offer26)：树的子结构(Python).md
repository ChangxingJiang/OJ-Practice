# LeetCode题解(Offer26)：判断二叉树A是否为二叉树B的子树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×H)$   | $O(N×H)$   | 112ms (94.89%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False

        def dfs1(a):
            if a:
                if a.val == B.val:
                    if dfs2(a.left, B.left) and dfs2(a.right, B.right):
                        self.ans = True
                dfs1(a.left)
                dfs1(a.right)

        def dfs2(a, b):
            if a and b:
                return a.val == b.val and dfs2(a.left, b.left) and dfs2(a.right, b.right)
            elif a:
                return True
            elif b:
                return False
            else:
                return True

        dfs1(A)

        return self.ans
```

