# LeetCode题解(1490)：克隆N叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/clone-n-ary-tree/)（中等）

标签：树、N叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 80ms (87.93%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None

        copy = Node(root.val)
        self.dfs(root, copy)
        return copy

    def dfs(self, node, copy):
        for node_child in node.children:
            copy_child = Node(node_child.val)
            self.dfs(node_child, copy_child)
            copy.children.append(copy_child)
```