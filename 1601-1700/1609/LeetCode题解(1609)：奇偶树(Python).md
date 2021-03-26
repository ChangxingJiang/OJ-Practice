# LeetCode题解(1609)：判断二叉树是否为奇偶树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/even-odd-tree/)（中等）

标签：树、二叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 612ms (49%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一（广度优先搜索）：

```python
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = deque([root])
        level = 0
        while queue:
            if level % 2 == 0:
                last_val = float("-inf")
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node.val % 2 == 0:
                        return False
                    if node.val <= last_val:
                        return False
                    last_val = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            else:
                last_val = float("inf")
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node.val % 2 == 1:
                        return False
                    if node.val >= last_val:
                        return False
                    last_val = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            level += 1

        return True
```