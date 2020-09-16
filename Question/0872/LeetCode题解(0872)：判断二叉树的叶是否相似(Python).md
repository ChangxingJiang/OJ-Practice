# LeetCode题解(0872)：判断二叉树的叶是否相似(Python)

题目：[原题链接](https://leetcode-cn.com/problems/leaf-similar-trees/)（简单）

| 解法           | 时间复杂度                                  | 空间复杂度                                  | 执行用时      |
| -------------- | ------------------------------------------- | ------------------------------------------- | ------------- |
| Ans 1 (Python) | $O(T_1+T_2)$ : $T_1$和$T_2$分别为两树的深度 | $O(T_1+T_2)$ : $T_1$和$T_2$分别为两树的深度 | 40ms (84.19%) |
| Ans 2 (Python) | $O(T_1+T_2)$ : $T_1$和$T_2$分别为两树的深度 | $O(T_1+T_2)$ : $T_1$和$T_2$分别为两树的深度 | 44ms (65.15%) |
| Ans 3 (Python) |                                             |                                             |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    def helper(node):
        if not node:
            return []
        if node.left and node.right:
            return helper(node.left) + helper(node.right)
        elif node.left:
            return helper(node.left)
        elif node.right:
            return helper(node.right)
        else:
            return [node.val]

    return helper(root1) == helper(root2)
```

解法二：

```python
def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    def helper(node):
        if node:
            if not node.left and not node.right:
                yield node.val
            yield from helper(node.left)
            yield from helper(node.right)

    return list(helper(root1)) == list(helper(root2))
```