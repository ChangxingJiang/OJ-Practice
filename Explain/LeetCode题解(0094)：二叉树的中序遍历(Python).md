# LeetCode题解(0094)：二叉树的中序遍历(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)（中等）

标签：树、二叉树、二叉树-遍历、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(logN)$  | 32ms (96.42%) |
| Ans 2 (Python) | $O(N)$     | $O(logN)$  | 28ms (99.19%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归）：

```python
def inorderTraversal(self, root: TreeNode) -> List[int]:
    if root:
        return self.inorder_traversal_to_iter(root.left) + [root.val] + self.inorder_traversal_to_iter(root.right)
    else:
        return []
```

解法二（迭代）：

```python
def inorderTraversal(self, root: TreeNode) -> List[int]:
    # 处理特殊情况
    if not root:
        return []

    stack = [root]
    ans = []
    while stack:
        if now := stack[-1]:
            stack.append(now.left)
        else:
            stack.pop()
            if not stack:
                break
            now = stack.pop()
            ans.append(now.val)
            stack.append(now.right)

    return ans
```