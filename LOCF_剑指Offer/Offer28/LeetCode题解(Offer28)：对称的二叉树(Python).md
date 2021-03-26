# LeetCode题解(Offer28)：判断二叉树是否左右对称(Python)

题目：[原题链接](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/)（简单）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (74.25%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(node1, node2):
            if node1 and node2:
                return node1.val == node2.val and dfs(node1.right, node2.left) and dfs(node1.left, node2.right)
            elif node1 or node2:
                return False
            else:
                return True

        return dfs(root.left, root.right) if root else True
```