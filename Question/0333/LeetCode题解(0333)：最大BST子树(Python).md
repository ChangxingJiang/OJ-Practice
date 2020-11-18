# LeetCode题解(0333)：最大BST子树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-bst-subtree/)（中等）

标签：树、二叉树、二叉搜索树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (98.02%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans_node, self.ans_num = None, 0

    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.dfs(root)

        return self.ans_num

    def dfs(self, node):
        # 返回值：是否为BST、包含的节点数量、最小值、最大值
        if node.left and node.right:
            left_bool, left_num, left_min, left_max = self.dfs(node.left)
            right_bool, right_num, right_min, right_max = self.dfs(node.right)
            if left_bool and right_bool and left_max < node.val < right_min:
                if self.ans_num < left_num + right_num + 1:
                    self.ans_node, self.ans_num = node, left_num + right_num + 1
                return True, left_num + right_num + 1, left_min, right_max
            else:
                return False, None, None, None
        elif node.left:
            left_bool, left_num, left_min, left_max = self.dfs(node.left)
            if left_bool and left_max < node.val:
                if self.ans_num < left_num + 1:
                    self.ans_node, self.ans_num = node, left_num + 1
                return True, left_num + 1, left_min, node.val
            else:
                return False, None, None, None
        elif node.right:
            right_bool, right_num, right_min, right_max = self.dfs(node.right)
            if right_bool and node.val < right_min:
                if self.ans_num < right_num + 1:
                    self.ans_node, self.ans_num = node, right_num + 1
                return True, right_num + 1, node.val, right_max
            else:
                return False, None, None, None
        else:
            if self.ans_num < 1:
                self.ans_node, self.ans_num = node, 1
            return True, 1, node.val, node.val
```