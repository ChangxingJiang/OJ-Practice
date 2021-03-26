# LeetCode题解(Offer36)：将二叉搜索树就地转换为双向链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/)（中等）

标签：树、二叉树、二叉搜索树、链表、分治算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (83.61%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（中序遍历二叉树）：

```python
class Solution:
    def __init__(self):
        self.last = None
        self.first = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node):
            if node:
                # 处理左子树
                dfs(node.left)

                # 处理当前节点
                if not self.last:
                    self.first = node
                    self.last = node
                else:
                    node.left = self.last
                    node.left.right = node
                    self.last = node

                # 处理右子树
                dfs(node.right)

        if root:
            dfs(root)

            self.last.right = self.first
            self.first.left = self.last

            return self.first
```