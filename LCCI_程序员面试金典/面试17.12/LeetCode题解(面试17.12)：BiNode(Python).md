# LeetCode题解(面试17.12)：BiNode(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binode-lcci/)（简单）

标签：树、二叉树、二叉搜索树、递归、链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(logN)$  | 92ms (99.84%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（递归）：

```python
class Solution:
    def convertBiNode(self, root: TreeNode, bigger=None) -> TreeNode:
        if root:
            # 处理当前节点
            left, right = root.left, root.right
            root.left = None

            # 处理当前节点的右侧节点
            if right:
                root.right = self.convertBiNode(right, bigger)
            else:
                root.right = bigger

            if left:
                return self.convertBiNode(left, root)
            else:
                return root
```