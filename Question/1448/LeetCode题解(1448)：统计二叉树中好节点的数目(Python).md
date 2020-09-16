# LeetCode题解(1448)：统计二叉树中好节点的数目(没有比自己的值大的父节点的节点为好节点)(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-good-nodes-in-binary-tree/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 332ms (43.65%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 288ms (81.76%) |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def goodNodes(self, root: TreeNode, last_max=-10001) -> int:
        if not root:
            return 0
        elif root.val >= last_max:
            return self.goodNodes(root.left, root.val) + self.goodNodes(root.right, root.val) + 1
        else:
            return self.goodNodes(root.left, last_max) + self.goodNodes(root.right, last_max)
```

解法二：

```python
class Solution:
    def __init__(self):
        self.ans = 0

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, last_max=-10001):
            if node:
                if node.val >= last_max:
                    self.ans += 1
                    dfs(node.left, node.val)
                    dfs(node.right, node.val)
                else:
                    dfs(node.left, last_max)
                    dfs(node.right, last_max)

        dfs(root)

        return self.ans
```