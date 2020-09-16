# LeetCode题解(0114)：将二叉树展开为只有右子树的链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/)（中等）

标签：树、二叉树、深度优先搜索、栈

| 解法           | 时间复杂度 | 空间复杂度                   | 执行用时      |
| -------------- | ---------- | ---------------------------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(H)$ : 其中H为二叉树的深度 | 52ms (51.47%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$                       | 48ms (75.21%) |
| Ans 3 (Python) |            |                              |               |

解法一（栈）：

```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        stack = []
        node = root
        while node:
            # 处理节点同时包含左右节点的情况
            if node.left and node.right:
                stack.append(node.right)
                node.left, node.right = None, node.left

            # 处理节点只包含左节点的情况
            elif node.left:
                node.left, node.right = None, node.left

            # 处理节点既没有左节点也没有右节点的情况（取出栈顶元素左右右节点）
            elif not node.right and stack:
                node.right = stack.pop()

            node = node.right
```

解法二（不使用栈存储，直接放到对应的树的位置上）

```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        node = root
        while node:
            if node.left:
                # 寻找当前右子树应移动到的位置
                now = node.left
                while now.right:
                    now = now.right

                # 移动当前右子树
                now.right = node.right

                # 修改当前节点
                node.left, node.right = None, node.left

            node = node.right
```