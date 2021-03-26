# LeetCode题解(0450)：删除二叉搜索树中的节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/delete-node-in-a-bst/)（中等）

标签：树、二叉树、二叉搜索树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(H)$     | $O(1)$     | 88ms (89.90%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # 寻找需要删除的节点
        def find(last_node, now_node):
            if not now_node:
                return None, None
            elif key == now_node.val:
                return last_node, now_node
            elif key < now_node.val:
                return find(now_node, now_node.left)
            elif key > now_node.val:
                return find(now_node, now_node.right)

        delete_node_father, delete_node = find(None, root)

        # 处理没有找到需要删除的节点的情况
        if not delete_node:
            return root

        left_branch = delete_node.left
        right_branch = delete_node.right

        # 执行删除操作
        if left_branch and right_branch:  # 处理两侧分支都存在的情况
            new_node = node = right_branch
            while node.left:
                node = node.left
            node.left = left_branch
        elif left_branch or right_branch:
            new_node = left_branch or right_branch
        else:
            new_node = None

        if not delete_node_father:
            return new_node
        elif delete_node_father.left and delete_node_father.left.val == key:
            delete_node_father.left = new_node
            return root
        else:
            delete_node_father.right = new_node
            return root
```