# LeetCode题解(0559)：计算N叉树的最大深度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (98.95%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归）：

```python
def maxDepth(self, root: 'Node') -> int:
    def helper(node):
        if not node:
            return 0
        if not node.children:
            return 1
        maximum = 0
        for child in node.children:
            maximum = max(maximum, helper(child))
        return maximum + 1

    return helper(root)
```