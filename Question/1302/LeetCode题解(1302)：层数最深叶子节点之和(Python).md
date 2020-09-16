# LeetCode题解(1302)：二叉树中层数最深的所有叶子节点之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/deepest-leaves-sum/)（中等）

标签：树、二叉树、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 104ms (95.04%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（广度优先搜索）：

```python
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ans = 0
        queue = collections.deque([root])
        while queue:
            ans = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                ans += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
```