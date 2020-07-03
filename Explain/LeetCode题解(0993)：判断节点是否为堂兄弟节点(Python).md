# LeetCode题解(0993)：判断节点是否为堂兄弟节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/cousins-in-binary-tree/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (83.55%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def __init__(self):
    self.depth = None
    self.father = None

def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    def helper(node, depth=0, father=None):
        if node:
            if node.val == x or node.val == y:
                if self.depth is None:
                    self.depth = depth + 1
                    self.father = father
                else:
                    if self.depth == depth + 1 and self.father != father:
                        return True
                    else:
                        return False
            return helper(node.left, depth + 1, node.val) or helper(node.right, depth + 1, node.val)

    return helper(root)
```