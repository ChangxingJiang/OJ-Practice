# LeetCode题解(0144)：二叉树的前序遍历(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)（中等）

标签：树、二叉树、二叉树-遍历、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(logN)$  | 40ms (70.49%) |
| Ans 2 (Python) | $O(N)$     | $O(logN)$  | 40ms (70.49%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归）：

```python
def preorderTraversal(self, root: TreeNode) -> List[int]:
    if root:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    else:
        return []
```

解法二（迭代）：

```python
def preorderTraversal(self, root: TreeNode) -> List[int]:
    # 处理特殊情况
    if not root:
        return []

    stack = [root]
    ans = []
    while stack:
        now = stack[-1]
        if now:
            ans.append(now.val)
            stack.append(now.left)
        else:
            stack.pop()
            if not stack:
                break
            now = stack.pop()
            stack.append(now.right)

    return ans
```