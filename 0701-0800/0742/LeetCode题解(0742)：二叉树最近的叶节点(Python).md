# LeetCode题解(0742)：二叉树最近的叶节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/closest-leaf-in-a-binary-tree/)（中等）

标签：树、二叉树、深度优先搜索、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 56ms (78.79%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（两次深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.hashmap = {}

    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        # 标记每个节点的子节点中的最近叶子节点
        # 时间:O(N) 空间:O(N)
        self.dfs1(root)

        # 寻找目标节点并计算最近的叶子节点
        # 时间:O(N) 空间:O(N)
        return self.dfs2(root, None, k)

    def dfs1(self, node):
        if node.left and node.right:
            d1, n1 = self.dfs1(node.left)
            d2, n2 = self.dfs1(node.right)
            if d1 <= d2:
                d, n = d1, n1
            else:
                d, n = d2, n2
            self.hashmap[node] = (d + 1, n)
            return d + 1, n
        elif node.left:
            d, n = self.dfs1(node.left)
            self.hashmap[node] = (d + 1, n)
            return d + 1, n
        elif node.right:
            d, n = self.dfs1(node.right)
            self.hashmap[node] = (d + 1, n)
            return d + 1, n
        else:
            d, n = 0, node.val
            self.hashmap[node] = (d, n)
            return d, n

    # 寻找目标节点并计算最近的叶子节点
    def dfs2(self, node, parent, k):
        if node:
            # 计算更新当前节点的最近叶子节点
            if parent:
                d1, n1 = self.hashmap[node]
                d2, n2 = self.hashmap[parent]
                if d1 > d2 + 1:
                    self.hashmap[node] = d2 + 1, n2

            # 寻找目标节点
            if node.val == k:
                return self.hashmap[node][1]
            else:
                return self.dfs2(node.left, node, k) or self.dfs2(node.right, node, k)

        else:
            return None
```