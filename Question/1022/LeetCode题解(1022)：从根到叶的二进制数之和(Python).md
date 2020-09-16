# LeetCode题解(1022)：从根到叶的二进制数之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/)（简单）

类似题目：129

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (71.55%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（遍历树）：

```python
def sumRootToLeaf(self, root: TreeNode) -> int:
    def helper(node, value=""):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return int(value + str(node.val), base=2)
        else:
            return helper(node.left, value + str(node.val)) + helper(node.right, value + str(node.val))

    return helper(root)
```