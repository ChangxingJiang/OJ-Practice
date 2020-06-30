# LeetCode题解(0589)：N叉树的前序遍历(Python)

题目：[原题链接](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/)（简单）

| 解法           | 时间复杂度 | 空间复杂度           | 执行用时      |
| -------------- | ---------- | -------------------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(d)$ : d为最大深度 | 64ms (71.32%) |
| Ans 2 (Python) |            |                      |               |
| Ans 3 (Python) |            |                      |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def preorder(self, root: 'Node') -> List[int]:
    def helper(node: 'Node'):
        if node is None:
            return []
        if node.children is None:
            return [node.val]
        ans = [node.val]
        for child in node.children:
            ans += helper(child)
        return ans

    return helper(root)
```