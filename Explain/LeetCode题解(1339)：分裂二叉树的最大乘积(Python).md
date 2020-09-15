# LeetCode题解(1339)：分裂一棵二叉树并使分裂成的两棵子树和的乘积最大(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-product-of-splitted-binary-tree/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 452ms (33.93%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 388ms (72.50%) |
| Ans 3 (Python) |            |            |                |

解法一（两次遍历）：

```python
class Solution:
    def __init__(self):
        self.max = 0

    def maxProduct(self, root: TreeNode) -> int:
        # 处理特殊情况
        if not root:
            return self.max

        # 计算子树和
        def dfs_sum(node):
            if node:
                if node.left:
                    dfs_sum(node.left)
                    node.val += node.left.val
                if node.right:
                    dfs_sum(node.right)
                    node.val += node.right.val

        dfs_sum(root)

        total = root.val

        # 计算最大乘积
        def dfs_count(node):
            if node:
                if node.left:
                    self.max = max(self.max, node.left.val * (total - node.left.val))
                    dfs_count(node.left)
                if node.right:
                    self.max = max(self.max, node.right.val * (total - node.right.val))
                    dfs_count(node.right)

        dfs_count(root)

        return self.max % (10 ** 9 + 7)
```

解法二（优化第二次遍历）：

```python
class Solution:
    def __init__(self):
        self.max = 0

    def maxProduct(self, root: TreeNode) -> int:
        # 处理特殊情况
        if not root:
            return self.max

        # 计算子树和
        def dfs_sum(node):
            if node:
                if node.left:
                    dfs_sum(node.left)
                    node.val += node.left.val
                if node.right:
                    dfs_sum(node.right)
                    node.val += node.right.val

        dfs_sum(root)

        total = root.val

        # 计算最大乘积
        def dfs_count(node):
            if node:
                if node.left:
                    a = node.left.val
                    b = total - node.left.val
                    self.max = max(self.max, a * b)
                    if a > b:
                        dfs_count(node.left)
                if node.right:
                    a = node.right.val
                    b = total - node.right.val
                    self.max = max(self.max, a * b)
                    if a > b:
                        dfs_count(node.right)

        dfs_count(root)

        return self.max % (10 ** 9 + 7)
```





