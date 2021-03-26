# LeetCode题解(1137)：二叉树中的列表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/linked-list-in-binary-tree/)（中等）

标签：二叉树、二叉树-深度优先遍历、链表

| 解法           | 时间复杂度 | 空间复杂度                   | 执行用时      |
| -------------- | ---------- | ---------------------------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(KlogN)$ : K为目标链表长度 | 96ms (99.54%) |
| Ans 2 (Python) |            |                              |               |
| Ans 3 (Python) |            |                              |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（存储所有当前可能情况）：

![LeetCode题解(1137)：截图1](LeetCode题解(1137)：截图1.png)

```python
def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
    def helper(node, maybe):
        # 处理当前节点为空的情况
        if not node:
            return False

        new_maybe = []
        for m in maybe:
            if node.val == m.val:
                if m.next is None:
                    return True
                new_maybe.append(m.next)
        if node.val == head.val:
            if head.next is None:
                return True
            new_maybe.append(head.next)

        return helper(node.left, new_maybe) or helper(node.right, new_maybe)

    return helper(root, [])
```