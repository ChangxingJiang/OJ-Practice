# LeetCode题解(Offer33)：判断整数数组是否可能为某二叉搜索树的后序遍历结果(Python)

题目：[原题链接](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)（中等）

标签：树、二叉树、数学、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (57.89%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（递归）：

```python
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True

        root = postorder[-1]
        left_post_order = []
        right_post_order = []
        for n in postorder[:-1]:
            if n < root:
                if not right_post_order:
                    left_post_order.append(n)
                else:
                    return False
            else:
                right_post_order.append(n)

        return self.verifyPostorder(left_post_order) and self.verifyPostorder(right_post_order)
```