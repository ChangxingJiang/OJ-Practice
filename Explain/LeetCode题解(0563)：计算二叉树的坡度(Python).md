# LeetCode题解(0563)：计算二叉树的坡度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-tilt/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 72ms (72.03%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def findTilt(self, root: TreeNode) -> int:
    def helper(node):
        if not node:
            return 0, 0

        slope_left, sum_left = helper(node.left)
        slope_right, sum_right = helper(node.right)

        slope_node = abs(sum_left - sum_right)
        sum_node = sum_left + sum_right + node.val
        slope_total = slope_left + slope_right + slope_node

        return slope_total, sum_node

    return helper(root)[0]
```