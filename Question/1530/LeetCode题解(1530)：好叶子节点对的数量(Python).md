# LeetCode题解(1530)：计算二叉树中距离在指定范围内的叶节点对数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-good-leaf-nodes-pairs/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 216ms (66.79%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.ans = 0

    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if node.left and node.right:
                left = dfs(node.left)
                right = dfs(node.right)
                for i in range(distance - 1):
                    for j in range(distance - 1 - i):
                        self.ans += left[i] * right[j]
                return [0] + [left[i] + right[i] for i in range(distance - 1)]
            elif node.left:
                left = dfs(node.left)
                return [0] + left[:-1]
            elif node.right:
                right = dfs(node.right)
                return [0] + right[:-1]
            else:
                return [1] + [0] * (distance - 2)

        dfs(root)

        return self.ans
```