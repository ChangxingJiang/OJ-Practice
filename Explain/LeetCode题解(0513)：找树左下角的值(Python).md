# LeetCode题解(0513)：寻找二叉树中最后一行左下角的值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-bottom-left-tree-value/)（中等）

标签：树、二叉树、深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 72ms (11.31%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 60ms (53.24%) |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:

    def __init__(self):
        self.level = 0
        self.ans = None

    def findBottomLeftValue(self, root: TreeNode) -> int:
        def recursor(node, level=1):
            if node:
                # 判断是否为答案
                if level > self.level:
                    self.ans = node.val
                    self.level = level

                recursor(node.left, level + 1)
                recursor(node.right, level + 1)

        recursor(root)

        return self.ans
```

解法二（层序遍历）：

```python
class Solution:

    def findBottomLeftValue(self, root: TreeNode) -> int:
        ans = root.val
        queue = collections.deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue:
                ans = queue[0].val

        return ans
```