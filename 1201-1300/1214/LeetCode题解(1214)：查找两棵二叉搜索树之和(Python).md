# LeetCode题解(1214)：查找两棵二叉搜索树之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/two-sum-bsts/)（中等）

标签：树、二叉树、二叉搜索树

| 解法           | 时间复杂度  | 空间复杂度  | 执行用时       |
| -------------- | ----------- | ----------- | -------------- |
| Ans 1 (Python) | $O(log^2N)$ | $O(log^2N)$ | 超出时间限制   |
| Ans 2 (Python) | $O(N1+N2)$  | $O(N1+N2)$  | 100ms (68.75%) |
| Ans 3 (Python) |             |             |                |

解法一：

```python
class Solution:
    def inorder(self, node, lst):
        if node:
            self.inorder(node.left, lst)
            lst.append(node.val)
            self.inorder(node.right, lst)

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        lst1, lst2 = [], []
        self.inorder(root1, lst1)
        self.inorder(root2, lst2)

        s1, s2 = len(lst1), len(lst2)
        i1, i2 = 0, s2 - 1

        while i1 < s1 and i2 >= 0:
            val = lst1[i1] + lst2[i2]
            if val < target:
                i1 += 1
            elif val > target:
                i2 -= 1
            else:
                return True

        return False
```