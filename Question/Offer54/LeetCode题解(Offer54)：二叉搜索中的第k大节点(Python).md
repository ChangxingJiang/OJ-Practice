# LeetCode题解(Offer54)：寻找二叉搜索树中的第k大节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)（简单）

标签：树、二叉树、二叉搜索树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(K+H)$   | $O(H)$     | 72ms (40.32%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（反向中序遍历）：

```python
class Solution:
    def __init__(self):
        self.idx = 0
        self.ans = 0

    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(node):
            if node:
                dfs(node.right)
                self.idx += 1
                if self.idx == k:
                    self.ans = node.val
                    return
                dfs(node.left)

        dfs(root)

        return self.ans
```