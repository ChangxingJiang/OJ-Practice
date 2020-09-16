# LeetCode题解(0958)：判断二叉树是否为完全二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/)（中等）

标签：树、二叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 36ms (98.28%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        already_finish = False
        queue = [root]
        for node in queue:
            if node.left:
                if already_finish:
                    return False
                queue.append(node.left)
            else:
                already_finish = True
            if node.right:
                if already_finish:
                    return False
                queue.append(node.right)
            else:
                already_finish = True

        return True
```