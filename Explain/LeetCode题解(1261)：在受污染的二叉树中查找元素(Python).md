# LeetCode题解(1261)：依据指定规则计算二叉树中的值并支持查找元素是否在二叉树中(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-elements-in-a-contaminated-binary-tree/)（中等）

标签：树、二叉树、深度优先搜索、集合

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 108ms (73.17%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class FindElements:

    def __init__(self, root: TreeNode):
        self.lst = set()

        def dfs(node, val):
            if node:
                self.lst.add(val)
                dfs(node.left, val * 2 + 1)
                dfs(node.right, val * 2 + 2)

        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.lst
```