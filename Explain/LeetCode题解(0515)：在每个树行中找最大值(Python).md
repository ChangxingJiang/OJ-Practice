# LeetCode题解(0515)：寻找二叉树中每一行的最大值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/)（中等）

标签：树、二叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (98.78%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # 处理特殊情况
        if not root:
            return []

        ans = []
        queue = collections.deque([root])

        while queue:
            max_val = float("-inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(max_val)

        return ans
```