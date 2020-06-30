# LeetCode题解(0590)：N叉树的后序遍历(Python)

题目：[原题链接](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)（简单）

| 解法           | 时间复杂度 | 空间复杂度                  | 执行用时      |
| -------------- | ---------- | --------------------------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(d)$ : d为N叉树的最大深度 | 60ms (84.54%) |
| Ans 2 (Python) |            |                             |               |
| Ans 3 (Python) |            |                             |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def postorder(self, root: 'Node') -> List[int]:
    def helper(node: "Node"):
        if node is None:
            return []
        if node.children is None:
            return [node.val]
        ans = []
        for child in node.children:
            ans += helper(child)
        ans += [node.val]
        return ans

    return helper(root)
```