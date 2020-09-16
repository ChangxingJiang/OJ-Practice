# LeetCode题解(0124)：计算二叉树中的最大路径和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)（困难）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 104ms (81.04%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 100ms (90.75%) |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def __init__(self):
        MOD = 10 ** 9 + 7
        self.max = -MOD

    def maxPathSum(self, root: TreeNode) -> int:
        self.count_max(root)
        return self.max

    def count_max(self, root: TreeNode) -> int:
        # 处理有两个子树的情况
        if root.left and root.right:
            left_max = self.count_max(root.left)
            right_max = self.count_max(root.right)
            if left_max >= 0 and right_max >= 0:
                self.max = max(self.max, root.val + left_max + right_max)
                return root.val + max(left_max, right_max)
            elif left_max >= 0:
                res_max = root.val + left_max
                self.max = max(self.max, res_max)
                return res_max
            elif right_max >= 0:
                res_max = root.val + right_max
                self.max = max(self.max, res_max)
                return res_max
            else:
                self.max = max(self.max, root.val)
                return root.val

        # 处理只有左子树的情况
        elif root.left:
            left_max = self.count_max(root.left)
            if left_max >= 0:
                res_max = root.val + left_max
                self.max = max(self.max, res_max)
                return res_max
            else:
                self.max = max(self.max, root.val)
                return root.val

        # 处理只有右子树的情况
        elif root.right:
            right_max = self.count_max(root.right)
            if right_max >= 0:
                res_max = root.val + right_max
                self.max = max(self.max, res_max)
                return res_max
            else:
                self.max = max(self.max, root.val)
                return root.val

        # 处理叶节点的情况
        else:
            self.max = max(self.max, root.val)
            return root.val
```

解法二（优化解法一）：

```python
class Solution:
    def __init__(self):
        MOD = 10 ** 9 + 7
        self.max = -MOD

    def maxPathSum(self, root: TreeNode) -> int:
        self.count_max(root)
        return self.max

    def count_max(self, node: TreeNode) -> int:
        if not node:
            return 0

        left_max = max(self.count_max(node.left), 0)
        right_max = max(self.count_max(node.right), 0)

        self.max = max(self.max, node.val + left_max + right_max)  # 更新最大路径和

        return node.val + max(left_max, right_max)  # 生成返回值
```



