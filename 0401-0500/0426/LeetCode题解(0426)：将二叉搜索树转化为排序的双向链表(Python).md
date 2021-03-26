# LeetCode题解(0426)：将二叉搜索树转化为排序的双向链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/)（中等）

标签：树、二叉树、二叉搜索树、链表、双向链表、分治算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (23.33%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（中序遍历二叉树）：

```python
class Solution:
    def __init__(self):
        self.last_node = None
        self.max_node = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 处理空树的特殊情况
        if not root:
            return None

        # 查找最大值节点
        # O(logN)
        node = root
        while node:
            self.last_node = node
            node = node.right

        self.max_node = self.last_node

        # 中序遍历调整二叉树
        self.dfs(root)

        return self.max_node.right

    def dfs(self, node):

        # print("START:", node.val,
        #       "(", node.left.val if node.left else None, node.right.val if node.right else None, ")")

        # 暂存当前节点的左右子节点
        left, right = node.left, node.right

        # 处理左子节点
        if left:
            self.dfs(left)

        # 处理当前节点
        self.last_node.right = node
        node.left = self.last_node
        self.last_node = node

        # 处理右子节点
        if right and node.val != self.max_node.val:
            self.dfs(right)

        # print("END:", node.val,
        #       "(", node.left.val if node.left else None, node.right.val if node.right else None, ")")
```