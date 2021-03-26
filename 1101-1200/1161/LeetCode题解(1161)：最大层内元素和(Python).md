# LeetCode题解(1161)：最大层内元素和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-level-sum-of-a-binary-tree/)（中等）

标签：树、二叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 312ms (81.97%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（层序遍历）：

```python
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = collections.deque([root])
        ans_idx, ans_val = 1, root.val
        level_idx = 1
        while level:
            level_val = 0
            for i in range(len(level)):
                p = level.popleft()
                level_val += p.val
                if p.left:
                    level.append(p.left)
                if p.right:
                    level.append(p.right)
            if ans_val < level_val:
                ans_idx, ans_val = level_idx, level_val
            level_idx += 1
        return ans_idx
```