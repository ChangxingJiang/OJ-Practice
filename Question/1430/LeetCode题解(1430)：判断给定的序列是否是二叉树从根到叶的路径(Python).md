# LeetCode题解(1430)：判断给定的序列是否是二叉树从根到叶的路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 104ms (98.28%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.arr = []

    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        self.arr = arr
        return self.dfs(root, 0)

    def dfs(self, node, i):
        if node and i < len(self.arr) and node.val == self.arr[i]:
            if i == len(self.arr)-1 and not node.left and not node.right:
                return True
            else:
                return self.dfs(node.left, i + 1) or self.dfs(node.right, i + 1)
        else:
            return False
```