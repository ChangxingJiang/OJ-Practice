# LeetCode题解(0129)：求根到所有叶子节点的数字之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (60.76%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 40ms (82.28%) |
| Ans 3 (Python) |            |            |               |

解法一（递归）：

```python
class Solution:
    def sumNumbers(self, root: TreeNode, now_val=0) -> int:
        # 处理当前节点不存在的情况
        if not root:
            return 0

        new_val = now_val * 10 + root.val

        # 处理当前节点非叶节点的情况
        if root.left or root.right:
            return self.sumNumbers(root.left, new_val) + self.sumNumbers(root.right, new_val)

        # 处理当前节点为叶节点的情况
        else:
            return new_val
```

解法二（优化解法一）：

```python
class Solution:
    def __init__(self):
        self.ans = 0

    def sumNumbers(self, root: TreeNode) -> int:
        self.count(root)
        return self.ans

    def count(self, node, now_val=0):
        if node:
            new_val = now_val * 10 + node.val
            if not node.left and not node.right:
                self.ans += new_val
            self.count(node.left, new_val)
            self.count(node.right, new_val)
```