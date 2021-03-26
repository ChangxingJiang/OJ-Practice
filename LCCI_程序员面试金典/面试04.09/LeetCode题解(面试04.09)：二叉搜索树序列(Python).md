# LeetCode题解(面试04.09)：二叉搜索树序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bst-sequences-lcci/)（困难）

标签：树、二叉树、二叉搜索树、回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(N^3)$   | 48ms (99.66%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        elif root.left and root.right:
            ans = []
            left_list = self.BSTSequences(root.left)
            right_list = self.BSTSequences(root.right)
            for left in left_list:
                for right in right_list:
                    size = len(left) + len(right)
                    for p in combinations([i for i in range(size)], len(right)):
                        right_idx = set(p)
                        lst = [root.val]
                        i1, i2 = 0, 0
                        for i in range(size):
                            if i not in right_idx:
                                lst.append(left[i1])
                                i1 += 1
                            else:
                                lst.append(right[i2])
                                i2 += 1
                        ans.append(lst)
            return ans
        elif root.left:
            ans = []
            for lst in self.BSTSequences(root.left):
                ans.append([root.val] + lst)
            return ans
        elif root.right:
            ans = []
            for lst in self.BSTSequences(root.right):
                ans.append([root.val] + lst)
            return ans
        else:
            return [[root.val]]
```