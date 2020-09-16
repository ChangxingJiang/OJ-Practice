# LeetCode题解(Offer34)：寻找二叉树中所有根节点到叶节点的路径和为目标值的路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(H)$     | 48ms (89.19%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.lst = []
        self.val = 0
        self.ans = []

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(node):
            if node:
                self.val += node.val
                self.lst.append(node.val)
                if node.left or node.right:
                    if node.left:
                        dfs(node.left)
                    if node.right:
                        dfs(node.right)
                else:
                    if self.val == sum:
                        self.ans.append(self.lst.copy())
                self.val -= node.val
                self.lst.pop()

        dfs(root)

        return self.ans
```