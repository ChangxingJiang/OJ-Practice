# LeetCode题解(0102)：二叉树的层次遍历(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)（中等）

标签：树、二叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (83.90%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 处理特殊情况
        if not root:
            return []

        ans = []
        now_node = [root]
        while now_node:
            now_val = []
            next_node = []
            for node in now_node:
                now_val.append(node.val)
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            ans.append(now_val)
            now_node = next_node

        return ans
```