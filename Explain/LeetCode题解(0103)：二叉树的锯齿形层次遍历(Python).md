# LeetCode题解(0103)：二叉树的锯齿形层次遍历(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)（中等）

标签：树、二叉树、二叉树-遍历

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(logN)$  | 32ms (98.36%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（reverse实现翻转）：

```python
def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    # 处理特殊情况
    if not root:
        return []

    order_is_left = True
    ans = []
    now_line = [root]
    while now_line:
        ans_line = []
        next_line = []
        for node in now_line:
            if node.left:
                next_line.append(node.left)
            if node.right:
                next_line.append(node.right)
            ans_line.append(node.val)

        if order_is_left:
            ans.append(ans_line)
        else:
            ans.append(list(reversed(ans_line)))

        now_line = next_line
        order_is_left = not order_is_left

    return ans
```



