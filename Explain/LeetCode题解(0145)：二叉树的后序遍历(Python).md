# LeetCode题解(0145)：二叉树的后序遍历(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)（困难）

标签：树、二叉树、二叉树-遍历、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(logN)$  | 40ms (70.91%) |
| Ans 2 (Python) | $O(N)$     | $O(logN)$  | 44ms (44.43%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归）：

```python
def postorderTraversal(self, root: TreeNode) -> List[int]:
    if root:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    else:
        return []
```

解法二（迭代）：

```python
def postorderTraversal(self, root: TreeNode) -> List[int]:
    # 处理特殊情况
    if not root:
        return []

    stack = [[root, False]]
    ans = []

    while stack:
        now = stack[-1]
        if now[0]:
            stack.append([now[0].left, False])
        else:
            stack.pop()
            if not stack:
                break
            now = stack[-1]
            if not now[1]:  # 右子树尚未遍历
                stack[-1][1] = True
                stack.append([now[0].right, False])
            else:  # 左右子树均已遍历
                ans.append(now[0].val)
                stack.pop()
                stack.append([None, True])

    return ans
```