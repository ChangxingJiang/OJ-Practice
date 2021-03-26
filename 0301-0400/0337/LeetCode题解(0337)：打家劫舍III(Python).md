# LeetCode题解(0337)：计算小偷在二叉树中不能偷取相邻房屋的前提下能够偷取的最高金额(Python)

题目：[原题链接](https://leetcode-cn.com/problems/house-robber-iii/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 64ms (66.67%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def rob(self, root: TreeNode) -> int:
        def recursor(node):
            # 处理当前节点不存在的情况
            if not node:
                return 0, 0

            # 左子树最大值(盗窃左节点和不盗窃左节点的两种情况)
            left1, left2 = recursor(node.left)

            # 右子树最大值(盗窃右节点和不盗窃右节点的两种情况)
            right1, right2 = recursor(node.right)

            # 盗窃当前节点并继续向根节点盗窃所能提供的最大值
            most_maybe1 = node.val + left2 + right2

            # 不盗窃当前节点并继续向根节点盗窃所能提供的最大值
            most_maybe2 = max(left1, left2) + max(right1, right2)  # 使用左子树和右子树的最大值，不盗窃当前节点

            return most_maybe1, most_maybe2

        return max(recursor(root))
```